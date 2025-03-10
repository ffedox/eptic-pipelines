import pandas as pd
import xml.etree.ElementTree as ET
import os
from bertalign import Bertalign

class AlignmentPipeline:
    def __init__(self, texts_path, xml_output_dir, alignments_path, output_excel):
        self.texts_path = texts_path
        self.xml_output_dir = xml_output_dir
        self.alignments_path = alignments_path
        self.output_excel = output_excel
        os.makedirs(xml_output_dir, exist_ok=True)

        self.existing_alignments = self._load_existing_alignments()
        self.alignment_records = []

    def _load_existing_alignments(self):
        if os.path.exists(self.alignments_path):
            df = pd.read_excel(self.alignments_path, dtype=str)
            existing_pairs = {}
            for _, row in df.iterrows():
                t1 = str(row['t1_id']).strip()
                t2 = str(row['t2_id']).strip()
                alignment_file = str(row['alignment_file']).strip()
                if t1 and t2 and alignment_file:
                    existing_pairs[frozenset([t1, t2])] = alignment_file
            return existing_pairs
        return {}

    def run(self):
        self.load_data()
        self.align_texts()
        self.save_alignments_to_excel()
        self.rename_xml_files()

    def load_data(self):
        if not os.path.exists(self.texts_path):
            return
        self.texts_data = pd.read_excel(self.texts_path, dtype={'id': str})
        self.texts_data.rename(columns={
            'id': 'id', 'event_id': 'event_id', 'lang': 'lang',
            'source_target': 'source_target', 'spoken_written': 'spoken_written',
            'sentence_split_text': 'sentence_split_text'
        }, inplace=True)
        self.texts_data['processed_text'] = self.texts_data['sentence_split_text'].apply(self._process_xml_sentences)

    @staticmethod
    def _process_xml_sentences(xml_str):
        if pd.isnull(xml_str):
            return ""
        try:
            root = ET.fromstring(xml_str)
            sentences = [s.text for s in root.findall('.//s') if s.text is not None]
            return '\n'.join(sentences)
        except ET.ParseError:
            return ""

    def align_texts(self):
        grouped = self.texts_data.groupby('event_id')
        for event_id, group in grouped:
            combinations = group.groupby(['lang', 'source_target', 'spoken_written'])
            for (lang1, source_target1, spoken_written1), group1 in combinations:
                for (lang2, source_target2, spoken_written2), group2 in combinations:
                    if (lang1, source_target1, spoken_written1) < (lang2, source_target2, spoken_written2):
                        if lang1 == "en" and source_target1 == "TT":
                            st_lang = group[group['source_target'] == "ST"]['lang'].unique()
                            if len(st_lang) > 0:
                                lang1_from = st_lang[0]
                                pair_name = (
                                    f"eptic_{lang1.lower()}_{spoken_written1.lower()}_{source_target1.lower()}_from_{lang1_from.lower()}."
                                    f"eptic_{lang2.lower()}_{spoken_written2.lower()}_{source_target2.lower()}"
                                )
                            else:
                                continue
                        else:
                            pair_name = (
                                f"eptic_{lang1.lower()}_{spoken_written1.lower()}_{source_target1.lower()}."
                                f"eptic_{lang2.lower()}_{spoken_written2.lower()}_{source_target2.lower()}"
                            )
                        for row1 in group1.itertuples(index=False):
                            for row2 in group2.itertuples(index=False):
                                pair = frozenset([str(row1.id).strip(), str(row2.id).strip()])
                                if pair in self.existing_alignments:
                                    alignment_data = self.existing_alignments[pair]
                                    self._generate_xml(pair_name, alignment_data, is_new=False)
                                else:
                                    alignment_result = self._align_sents(row1.id, row2.id, lang1, lang2)
                                    if alignment_result:
                                        xml_string = "\n".join([
                                            f"<link type='{res['type']}' xtargets='{res['xtargets']}' status='{res['status']}'/>".replace('"', "'")
                                            for res in alignment_result
                                        ])
                                        self._generate_xml(pair_name, xml_string, is_new=True)
                                self.alignment_records.append({
                                    't1_id': row1.id,
                                    't2_id': row2.id,
                                    'alignment_file': alignment_data if pair in self.existing_alignments else xml_string
                                })
    
    def _align_sents(self, src_id, tgt_id, src_lang, tgt_lang):
        src_text = self.texts_data.loc[self.texts_data['id'] == src_id, 'processed_text'].values[0]
        tgt_text = self.texts_data.loc[self.texts_data['id'] == tgt_id, 'processed_text'].values[0]
        if not src_text or not tgt_text:
            return None
        aligner = Bertalign(src_text, tgt_text, src_lang=src_lang, tgt_lang=tgt_lang)
        aligner.align_sents()
        alignments, _ = aligner.get_result()
        results = []
        for left_side, right_side in alignments:
            src_targets = ' '.join([f"{src_id}:{idx + 1}" for idx in left_side])
            tgt_targets = ' '.join([f"{tgt_id}:{idx + 1}" for idx in right_side])
            results.append({"src_id": src_id, "tgt_id": tgt_id, "xtargets": f"{src_targets};{tgt_targets}", "type": f"{len(left_side)}-{len(right_side)}", "status": "auto"})
        return results

    def rename_xml_files(self):
        """
        Scans all output XMLs and renames files matching the pattern:
        - Files containing '.eptic_en_wr_tt.xml' will be renamed to 
        '.eptic_en_wr_tt_from_XX.xml' where XX is extracted from 
        'eptic_en_sp_tt_from_XX.' in the same filename
        """

        file_count = 0
        
        for filename in os.listdir(self.xml_output_dir):
            if '.eptic_en_wr_tt.xml' in filename:
                # Look for the source language in the same filename
                search_pattern = 'eptic_en_sp_tt_from_'
                if search_pattern in filename:
                    # Find what comes between 'eptic_en_sp_tt_from_' and '.'
                    start_idx = filename.find(search_pattern) + len(search_pattern)
                    end_idx = filename.find('.', start_idx)
                    
                    if start_idx > 0 and end_idx > start_idx:
                        source_lang = filename[start_idx:end_idx]
                        
                        # Create the new filename
                        new_filename = filename.replace(
                            '.eptic_en_wr_tt.xml',
                            f'.eptic_en_wr_tt_from_{source_lang}.xml'
                        )
                        
                        # Rename the file
                        old_path = os.path.join(self.xml_output_dir, filename)
                        new_path = os.path.join(self.xml_output_dir, new_filename)
                        os.rename(old_path, new_path)
                        file_count += 1        

    def _generate_xml(self, pair_name, alignment_data, is_new=False):
        output_path = os.path.join(self.xml_output_dir, f"{pair_name}.xml")
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                existing_content = f.read().strip()
            if existing_content.endswith("</linkGrp>"):
                existing_content = existing_content[:-10].strip()
            new_content = existing_content + "\n" + alignment_data.strip() + "\n</linkGrp>"
        else:
            new_content = (
                "<?xml version='1.0' encoding='utf-8'?>\n"
                "<linkGrp toDoc='placeholder_toDoc.xml' fromDoc='placeholder_fromDoc.xml'>\n"
                + alignment_data.strip() + "\n</linkGrp>"
            )
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(new_content.replace('"', "'"))

    def save_alignments_to_excel(self):
        df = pd.DataFrame(self.alignment_records)
        df.to_excel(self.output_excel, index=False)

if __name__ == "__main__":
    texts_path = input("Enter the path to texts.xlsx: ").strip()
    alignments_path = input("Enter the path to alignments.xlsx: ").strip()
    output_excel = input("Enter the path to save alignments.xlsx: ").strip()
    pipeline = AlignmentPipeline(
        texts_path=texts_path,
        xml_output_dir='/home/afedotova/EPTIC25/eptic.v5/2. bertalign_alignments',
        alignments_path=alignments_path,
        output_excel=output_excel
    )
    pipeline.run()
