import pandas as pd
from xml.etree.ElementTree import Element, SubElement, tostring, fromstring, ParseError, parse, ElementTree
import re
import os
from bertalign import Bertalign

class AlignmentPipeline:
    def __init__(self, texts_path, xml_output_dir):
        self.texts_path = texts_path
        self.xml_output_dir = xml_output_dir
        os.makedirs(xml_output_dir, exist_ok=True)
    
    def run(self):
        """Execute the pipeline."""
        self.load_data()
        self.align_texts()
        self.save_alignments_to_excel()

    def load_data(self):
        """Load and preprocess input data."""
        self.texts_data = pd.read_excel(self.texts_path, dtype={'texts.id': str})
        self.texts_data.rename(columns={
            'texts.id': 'id',
            'texts.event_id': 'event_id',
            'texts.lang': 'lang',
            'texts.source_target': 'source_target',
            'texts.spoken_written': 'spoken_written',
            'texts.sentence_split_text': 'sentence_split_text'
        }, inplace=True)

        # Process sentence_split_text into processed_text
        self.texts_data['processed_text'] = self.texts_data['sentence_split_text'].apply(self._process_xml_sentences)
        print("Data loaded and processed.")

    @staticmethod
    def _process_xml_sentences(xml_str):
        """Extract text content from XML sentences."""
        if pd.isnull(xml_str):
            return ""
        try:
            root = fromstring(xml_str)
            sentences = [s.text for s in root.findall('.//s') if s.text is not None]
            return '\n'.join(sentences)
        except ParseError:
            return ""

    def align_texts(self):
        """Align texts and save results in memory."""
        grouped = self.texts_data.groupby('event_id')

        print("Aligning files...")

        for event_id, group in grouped:
            combinations = group.groupby(['lang', 'source_target', 'spoken_written'])

            for (lang1, src_target1, spoken_written1), group1 in combinations:
                for (lang2, src_target2, spoken_written2), group2 in combinations:
                    if (lang1, src_target1, spoken_written1) < (lang2, src_target2, spoken_written2):
                        pair_name = (
                            f"EPTIC.{lang1.lower()}_{spoken_written1.lower()}_{src_target1.lower()}."
                            f"{lang2.lower()}_{spoken_written2.lower()}_{src_target2.lower()}"
                        )
                        alignment_results = []

                        for row1 in group1.itertuples(index=False):
                            for row2 in group2.itertuples(index=False):
                                alignment_result = self._align_sents(row1.id, row2.id, lang1, lang2)
                                if alignment_result:
                                    alignment_results.extend(alignment_result)

                        if alignment_results:
                            self._generate_xml(pair_name, alignment_results)

    def _align_sents(self, src_id, tgt_id, src_lang, tgt_lang):
        """Align sentences using Bertalign."""
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
            results.append({
                "src_id": src_id,
                "tgt_id": tgt_id,
                "xtargets": f"{src_targets};{tgt_targets}",
                "type": f"{len(left_side)}-{len(right_side)}",
                "status": "auto"
            })

        return results

    def _generate_xml(self, pair_name, alignment_results):
        """Generate or append XML for all alignments of a pair."""
        output_path = os.path.join(self.xml_output_dir, f"{pair_name}.xml")

        # Check if the file already exists
        if os.path.exists(output_path):
            tree = parse(output_path)
            root = tree.getroot()
        else:
            root = Element('linkGrp', attrib={'toDoc': 'placeholder_toDoc.xml', 'fromDoc': 'placeholder_fromDoc.xml'})

        # Append new alignment results
        for result in alignment_results:
            SubElement(root, 'link', attrib={
                'type': result['type'],
                'xtargets': result['xtargets'],
                'status': result['status']
            })

        xml_content = self._prettify_and_refine_xml(tostring(root, encoding='unicode'))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)


    def save_alignments_to_excel(self):
        """Save alignments to an Excel file."""
        alignment_data = []

        for xml_file in os.listdir(self.xml_output_dir):
            if xml_file.endswith('.xml'):
                xml_path = os.path.join(self.xml_output_dir, xml_file)
                try:
                    tree = parse(xml_path)
                    root = tree.getroot()

                    for link in root.findall('link'):
                        xtargets = link.attrib.get('xtargets', '')
                        src_targets, tgt_targets = xtargets.split(';')

                        src_id = src_targets.split(':')[0]
                        tgt_id = tgt_targets.split(':')[0]

                        alignment_file = tostring(root, encoding='unicode')

                        alignment_data.append({
                            't1_id': src_id,
                            't2_id': tgt_id,
                            'alignment_file': alignment_file
                        })

                except (ParseError, ValueError) as e:
                    print(f"Failed to parse {xml_path} due to {e}, skipping...")

        alignment_df = pd.DataFrame(alignment_data, columns=['t1_id', 't2_id', 'alignment_file'])
        output_excel_path = "/home/afedotova/EPTIC25/eptic25_v1/1. database_tables/alignments.xlsx"
        alignment_df.to_excel(output_excel_path, index=False)
        print(f"Alignments saved to {output_excel_path}")

    @staticmethod
    def _prettify_and_refine_xml(xml_string):
        """Prettify and clean the XML output."""
        xml_string = AlignmentPipeline._rearrange_link_attributes(xml_string)
        xml_string = re.sub(r'>\s*<', '>\n<', xml_string).strip()
        xml_string = xml_string.replace('"', "'")
        return f"<?xml version='1.0' encoding='utf-8'?>\n{xml_string}"

    @staticmethod
    def _rearrange_link_attributes(xml_string):
        """Rearrange attributes in <link> tags."""
        tree = ElementTree(fromstring(xml_string))
        root = tree.getroot()
        for link in root.findall('.//link'):
            attributes = link.attrib
            ordered_attributes = {k: attributes.pop(k) for k in ['type', 'xtargets', 'status'] if k in attributes}
            link.attrib.clear()
            link.attrib.update(ordered_attributes)
        return tostring(root, encoding='unicode').replace(' />', '/>')


if __name__ == "__main__":
    pipeline = AlignmentPipeline(
        texts_path='/home/afedotova/EPTIC25/eptic25_v1/1. database_tables/texts.xlsx',
        xml_output_dir='/home/afedotova/EPTIC25/test_pretgds'
    )
    pipeline.run()
