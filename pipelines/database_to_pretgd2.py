import pandas as pd
import re
import os
from lxml import etree

# Directory paths
output_folder_path = '/home/afedotova/EPTIC25/eptic.v4/3. pre_pos_files'

# Load the provided Excel files 
texts_file_path = '/home/afedotova/EPTIC25/eptic.v4/1. database_tables/texts.xlsx'
events_file_path = '/home/afedotova/EPTIC25/eptic.v4/1. database_tables/events.xlsx'
speakers_file_path = '/home/afedotova/EPTIC25/eptic.v4/1. database_tables/speakers.xlsx'
interpreters_file_path = '/home/afedotova/EPTIC25/eptic.v4/1. database_tables/interpreters.xlsx'

# Load supporting data
texts_df = pd.read_excel(texts_file_path)
events_df = pd.read_excel(events_file_path)
speakers_df = pd.read_excel(speakers_file_path)
interpreters_df = pd.read_excel(interpreters_file_path)

# Ensure the renaming logic is correctly applied
# Adjust DataFrame columns to match expected keys
for df in [texts_df, events_df, speakers_df, interpreters_df]:
    df.columns = [col.replace(".", "_").lower().replace(" ", "_") for col in df.columns]

# Define full names for languages
language_full_names = {
    "DE": "German", "EN": "English", "FR": "French",
    "IT": "Italian", "PL": "Polish", "FI": "Finnish", "SL": "Slovenian"
}

# Define possible combinations
combinations = {
    "TT SP": "interpretations", "TT WR": "translations",
    "ST SP": "spoken sources", "ST WR": "written sources"
}

# Generate exhaustive type mapping
type_mapping = {}
for lang_code, lang_full in language_full_names.items():
    for combo, combo_full in combinations.items():
        key = f"{lang_code} {combo}"
        value = f"{lang_full} {combo_full}"
        type_mapping[key] = value

def map_type_value(type_key):
    # Attempt to map the type_key directly
    mapped_value = type_mapping.get(type_key)
    if not mapped_value:
        print(f"Mapping not found for: {type_key}")  # Debug message
    return mapped_value or type_key

def na_if_nan(value):
    """Returns 'NA' if value is NaN or None, otherwise returns the value itself."""
    if pd.isna(value):
        return "NA"
    return value

def preprocess_xml(xml_str):
    """
    Preprocesses the XML string by removing the Byte Order Mark (BOM) if present, 
    trimming leading whitespace, and escaping unescaped ampersands that aren't part of an entity.
    """
    # Remove UTF-8 BOM if present
    xml_str = xml_str.lstrip('\ufeff')
    # Strip leading whitespace characters
    xml_str = xml_str.lstrip()
    
    # Escape unescaped ampersands that aren't part of an entity
    # This regex looks for & that isn't followed by an entity pattern (name;)
    import re
    xml_str = re.sub(r'&(?!(amp|lt|gt|apos|quot|#\d+|#x[0-9a-fA-F]+);)', '&amp;', xml_str)
    
    return xml_str

def parse_xml_s_tags(xml_str, video_url=None):
    if not xml_str or pd.isna(xml_str):
        return []
        
    xml_str_cleaned = preprocess_xml(xml_str)
    
    try:
        # Parse the cleaned XML string directly using lxml
        root = etree.fromstring(xml_str_cleaned.encode('utf-8'))
        s_elements = root.findall(".//s")
        return [{"id": s.get("id"), "text": s.text} for s in s_elements]
    except etree.XMLSyntaxError as e:
        # Try an alternative approach with a more lenient parser
        try:
            from xml.dom import minidom
            # For really problematic XML, try to extract the s tags manually
            s_tags = []
            # Use regex to extract s tags and their content
            import re
            pattern = r'<s id="([^"]+)"[^>]*>(.*?)<\/s>'
            matches = re.findall(pattern, xml_str_cleaned, re.DOTALL)
            if matches:
                for match in matches:
                    s_tags.append({"id": match[0], "text": match[1].strip()})
                return s_tags
            else:
                print(f"XML parsing error using lxml and backup method failed: {e}\nProblematic XML content:\n{xml_str}")
                return []
        except Exception as ex:
            print(f"Both XML parsing methods failed: {ex}\nProblematic XML content:\n{xml_str}")
            return []

def match_subtitles_with_timestamps(subtitled_text, s_tags, video_url, text_id):
    # Handle empty s_tags
    if not s_tags:
        print(f"Warning: No s_tags found for text_id {text_id}")
        return s_tags
        
    # Parse subtitled text to get timestamps
    subtitle_parts = subtitled_text.strip().split("\n\n")
    timestamps = []
    for part in subtitle_parts:
        lines = part.split("\n")
        if len(lines) >= 3:
            timestamp_line = lines[1]
            try:
                start, end = re.findall(r"(\d{2}:\d{2}:\d{2}),\d+", timestamp_line)
                timestamps.append({"start": start, "end": end})
            except ValueError:
                # In case the regex doesn't find exactly two matches
                print(f"Warning: Could not parse timestamp line: {timestamp_line}")
                continue
    
    # Handle mismatch in number of s_tags and timestamps
    if len(s_tags) != len(timestamps):
        print(f"Warning: Mismatch in {text_id}: s_tags ({len(s_tags)}) and subtitle timestamps ({len(timestamps)}). Using available timestamps.")
        # Use as many timestamps as available, or generate placeholders
        if len(timestamps) == 0:
            # No timestamps found, return original s_tags without video info
            return s_tags
        
        # If we have fewer timestamps than s_tags, use the available ones and then repeat the last one
        while len(timestamps) < len(s_tags):
            if timestamps:  # If we have at least one timestamp
                timestamps.append(timestamps[-1])  # Repeat the last timestamp
            else:
                # Create a placeholder timestamp if none exist
                timestamps.append({"start": "00.00.00", "end": "00.00.00"})
                
        # If we have more timestamps than s_tags, truncate timestamps
        timestamps = timestamps[:len(s_tags)]
    
    # Match s_tags with timestamps based on order
    matched_s_tags = []
    for s_tag, timestamp in zip(s_tags, timestamps):
        matched_s_tags.append({
            "id": s_tag["id"],
            "text": s_tag["text"],
            "start": timestamp["start"].replace(":", "."),
            "end": timestamp["end"].replace(":", "."),
            "video_url": video_url
        })

    return matched_s_tags

def create_vert_structure(text_id, texts_df, events_df, speakers_df, interpreters_df):
    text_row = texts_df[texts_df["texts_id"] == text_id].iloc[0]
    # Check for NaN values in critical fields
    if pd.isna(text_row["texts_duration"]) or pd.isna(text_row["texts_word_count"]):
        return None  # Skip this record
    
    # Proceed with processing if no critical NaN values are found
    event_row = events_df[events_df["events_id"] == text_row["texts_event_id"]].iloc[0]
    if event_row.empty:
        return None  # Skip if the event row is missing
    
    speaker_row = speakers_df[speakers_df["speakers_id"] == event_row["events_speaker_id"]].iloc[0]
    if speaker_row.empty:
        return None  # Skip if the speaker row is missing
    
    interpreter_id = text_row["texts_interpreter_id"]
    interpreter_row = interpreters_df[interpreters_df["interpreters_id"] == interpreter_id] if pd.notnull(interpreter_id) else pd.DataFrame()
    
    # Finding the related WR and ST row for the event
    related_text_row = texts_df[(texts_df["texts_event_id"] == text_row["texts_event_id"]) & 
                                (texts_df["texts_spoken_written"] == "WR") & 
                                (texts_df["texts_source_target"] == "ST")].iloc[0] if not texts_df[(texts_df["texts_event_id"] == text_row["texts_event_id"]) & 
                                (texts_df["texts_spoken_written"] == "WR") & 
                                (texts_df["texts_source_target"] == "ST")].empty else None

    if related_text_row is not None:
        st_language = related_text_row["texts_lang"]
        st_lengthw = related_text_row["texts_word_count"]
        st_length = "short" if 100 <= st_lengthw <= 400 else "medium" if 401 <= st_lengthw <= 1000 else "long"
        st_durations = related_text_row["texts_duration"]
        st_duration = "short" if st_durations < 120 else "medium" if 120 <= st_durations <= 360 else "long"
        st_speedwm = round(st_lengthw / (st_durations / 60), 1) if st_durations > 0 else 0
        st_speed = "slow" if st_speedwm < 130 else "medium" if 130 <= st_speedwm <= 160 else "high"
        st_delivery = event_row["events_delivery"]
    else:
        st_language = "NA"
        st_lengthw = "NA"
        st_length = "NA"
        st_durations = "NA"
        st_duration = "NA"
        st_speedwm = "NA"
        st_speed = "NA"
        st_delivery = "NA"

    s_tags = parse_xml_s_tags(text_row["texts_sentence_split_text"])
    
    type_key = f"{text_row['texts_lang'].upper()} {text_row['texts_source_target']} {text_row['texts_spoken_written']}"
    type_value = map_type_value(type_key)
    
    word_count = text_row["texts_word_count"]
    durations = round(float(text_row["texts_duration"]), 0)
    length_category = "short" if 100 <= word_count <= 400 else "medium" if 401 <= word_count <= 1000 else "long"
    duration_category = "short" if durations < 120 else "medium" if 120 <= durations <= 360 else "long"
    words_per_minute = round(word_count / (durations / 60), 1)
    speed_category = "slow" if words_per_minute < 130 else "medium" if 130 <= words_per_minute <= 160 else "high"
    
    event_date_str = "NA" if pd.isna(event_row["events_date"]) else event_row["events_date"].strftime("%Y-%m-%d")
    vert_string = f'<text id="{text_id}" date="{event_date_str}" length="{na_if_nan(length_category)}" lengthw="{na_if_nan(text_row["texts_word_count"])}" duration="{na_if_nan(duration_category)}" durations="{na_if_nan(round(float(text_row["texts_duration"]), 0))}" speed="{na_if_nan(speed_category)}" speedwm="{na_if_nan(words_per_minute)}" delivery="{na_if_nan(event_row["events_delivery"])}" topic="{na_if_nan(event_row["events_topic"])}" topicspec="{na_if_nan(event_row["events_topic_specific"])}" type="{na_if_nan(type_value)}" comments="NA">\n'
    vert_string += f'<speaker name="{na_if_nan(speaker_row["speakers_full_name"])}" gender="{na_if_nan(speaker_row["speakers_gender"])}" country="{na_if_nan(speaker_row["speakers_country"])}" politfunc="{na_if_nan(speaker_row["speakers_political_function"])}" politgroup="{na_if_nan(speaker_row["speakers_political_group"])}">\n'
    vert_string += f'<st language="{na_if_nan(st_language)}" length="{na_if_nan(st_length)}" lengthw="{na_if_nan(st_lengthw)}" duration="{na_if_nan(st_duration)}" durations="{na_if_nan(st_durations)}" speed="{na_if_nan(st_speed)}" speedwm="{na_if_nan(st_speedwm)}" delivery="{na_if_nan(st_delivery)}">\n'
    
    # Check if an interpreter ID is present and fetch the corresponding row
    if pd.notnull(text_row["texts_interpreter_id"]):
        interpreter_row = interpreters_df[interpreters_df["interpreters_id"] == text_row["texts_interpreter_id"]]
        interpreter_present = not interpreter_row.empty
    else:
        interpreter_present = False

    if interpreter_present:
        # If interpreter_row is not empty, meaning there's an interpreter
        interpreter_tag = f'<interpreter id="{na_if_nan(interpreter_row.iloc[0]["interpreters_nickname"])}" gender="{na_if_nan(interpreter_row.iloc[0]["interpreters_gender"])}" native="{na_if_nan(interpreter_row.iloc[0].get("interpreters_native", "NA"))}">\n'
    else:
        # If there's no interpreter assigned, include a placeholder or simplified tag
        interpreter_tag = '<interpreter id="NA" gender="NA" native="NA">\n'

    # Include the interpreter_tag when constructing the vert_string
    vert_string += interpreter_tag

    s_tags = parse_xml_s_tags(text_row["texts_sentence_split_text"])
    if text_row["texts_spoken_written"] == "SP" and pd.notnull(text_row["texts_subtitled_text"]) and pd.notnull(text_row["texts_video_url"]):
        try:
            # Assuming your code here calls match_subtitles_with_timestamps at some point
            s_tags = match_subtitles_with_timestamps(text_row["texts_subtitled_text"], s_tags, text_row["texts_video_url"], text_id)
        except ValueError as e:
            print(e)
            video_url = "ERR" 

    for s_tag in s_tags:
        video_attr = f' video="{s_tag["video_url"]}&start={s_tag["start"]}&end={s_tag["end"]}"' if "video_url" in s_tag else ""
        vert_string += f'<s id="{s_tag["id"]}"{video_attr}>\n{s_tag["text"]}\n</s>\n'

    # Ensure to append '</st>\n</speaker>\n</text>\n' after adding the interpreter tag
    vert_string += '</interpreter>\n</st>\n</speaker>\n</text>'
    return vert_string

def ensure_directory_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def find_source_language(texts_df, event_id):
    """Find the source language for a given event ID."""
    source_row = texts_df[(texts_df["texts_event_id"] == event_id) & 
                         (texts_df["texts_source_target"] == "ST")]
    if not source_row.empty:
        return source_row.iloc[0]["texts_lang"]
    return None

def generate_pretgd_files():
    ensure_directory_exists(output_folder_path)
    
    # Get unique combinations of lang, source_target, and spoken_written
    unique_combinations = texts_df.groupby(["texts_lang", "texts_source_target", "texts_spoken_written"]).size().reset_index(name="count")
    
    # Process each unique combination
    for _, combo in unique_combinations.iterrows():
        lang = combo["texts_lang"]
        source_target = combo["texts_source_target"]
        spoken_written = combo["texts_spoken_written"]
        
        # Check if it's one of the exception cases
        if (lang == "en" and source_target == "TT" and spoken_written == "SP") or \
           (lang == "en" and source_target == "TT" and spoken_written == "WR"):
            
            # Get all text IDs for this exception case
            text_ids = texts_df[
                (texts_df["texts_lang"] == lang) & 
                (texts_df["texts_source_target"] == source_target) & 
                (texts_df["texts_spoken_written"] == spoken_written)
            ]["texts_id"].tolist()
            
            # Group text_ids by source language
            source_lang_groups = {}
            for text_id in text_ids:
                text_row = texts_df[texts_df["texts_id"] == text_id].iloc[0]
                event_id = text_row["texts_event_id"]
                source_lang = find_source_language(texts_df, event_id)
                
                if source_lang:
                    if source_lang not in source_lang_groups:
                        source_lang_groups[source_lang] = []
                    source_lang_groups[source_lang].append(text_id)
            
            # Create .pretgd files for each source language group
            for source_lang, grouped_text_ids in source_lang_groups.items():
                # Determine the output filename
                if spoken_written == "SP":
                    output_filename = f"en_sp_tt_from_{source_lang.lower()}.pretgd"
                else:  # WR
                    output_filename = f"en_wr_tt_from_{source_lang.lower()}.pretgd"
                
                # Generate vert content for each text_id
                aggregated_content = []
                for text_id in grouped_text_ids:
                    vert_content = create_vert_structure(text_id, texts_df, events_df, speakers_df, interpreters_df)
                    if vert_content:
                        aggregated_content.append(vert_content)
                
                # Write to file if there's content
                if aggregated_content:
                    output_file_path = os.path.join(output_folder_path, output_filename)
                    with open(output_file_path, 'w', encoding='utf-8') as file:
                        file.write("\n".join(aggregated_content))
                    print(f"Generated {output_filename} with {len(aggregated_content)} text entries")
        
        else:
            # Standard case - create one file for this combination
            output_filename = f"{lang.lower()}_{spoken_written.lower()}_{source_target.lower()}.pretgd"
            
            # Get all text IDs for this combination
            text_ids = texts_df[
                (texts_df["texts_lang"] == lang) & 
                (texts_df["texts_source_target"] == source_target) & 
                (texts_df["texts_spoken_written"] == spoken_written)
            ]["texts_id"].tolist()
            
            # Generate vert content for each text_id
            aggregated_content = []
            for text_id in text_ids:
                vert_content = create_vert_structure(text_id, texts_df, events_df, speakers_df, interpreters_df)
                if vert_content:
                    aggregated_content.append(vert_content)
            
            # Write to file if there's content
            if aggregated_content:
                output_file_path = os.path.join(output_folder_path, output_filename)
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.write("\n".join(aggregated_content))
                print(f"Generated {output_filename} with {len(aggregated_content)} texts")

# Execute the refactored code
if __name__ == "__main__":
    generate_pretgd_files()