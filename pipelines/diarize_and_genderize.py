import os
import shutil
import subprocess
import tempfile
import pandas as pd
import torch
import torchaudio
import csv
import numpy as np
import datetime
import random
import glob
from collections import Counter
from torch import nn
from torchaudio.transforms import Resample
from pydub import AudioSegment
from pyannote.audio import Pipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook
from transformers import Wav2Vec2Processor
from transformers.models.wav2vec2.modeling_wav2vec2 import (
    Wav2Vec2Model,
    Wav2Vec2PreTrainedModel,
)

# -----------------------------------------------------
# PART 1: CONFIGURATION AND SETUP
# -----------------------------------------------------
print("### STARTING COMBINED PROCESSING PIPELINE ###")

# Configuration
BASE_VIDEO_FOLDER = input("Enter the full path to the video folder: ").strip()
AUDIO_FOLDER = os.path.join(BASE_VIDEO_FOLDER, "audio")
EXCEL_FILE = input("Enter the full path to the texts Excel file: ").strip()
OUTPUT_BASE_FOLDER = BASE_VIDEO_FOLDER
SILENCE_FILE = input("Enter the full path to the silence file: ").strip()

# Ensure output and audio folder exist
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# -----------------------------------------------------
# PART 2: AUDIO EXTRACTION AND ORGANIZATION
# -----------------------------------------------------
print("\n### STEP 1: EXTRACTING AUDIO FROM VIDEOS ###")

# Extract Audio from Videos (Skip if Audio Folders Exist)
if any(os.path.isdir(os.path.join(AUDIO_FOLDER, folder)) for folder in os.listdir(AUDIO_FOLDER)):
    print("Audio folders already exist. Skipping audio extraction.")
else:
    video_extensions = (".mp4", ".wmv")
    for file in os.listdir(BASE_VIDEO_FOLDER):
        if file.endswith(video_extensions):
            video_path = os.path.join(BASE_VIDEO_FOLDER, file)
            audio_path = os.path.join(AUDIO_FOLDER, os.path.splitext(file)[0] + ".mp3")
            subprocess.run(["ffmpeg", "-y", "-i", video_path, "-q:a", "0", "-map", "a", audio_path], check=True)
    print("Audio extraction completed.")

print("\n### STEP 2: ORGANIZING AUDIO FILES BY LANGUAGE ###")

# Organize Audio Files by Language
if not os.path.exists(EXCEL_FILE):
    print("Excel file not found!")
    exit(1)
df = pd.read_excel(EXCEL_FILE)
df['id'] = df['id'].astype(str)
for lang in df['lang'].unique():
    lang_dir = os.path.join(AUDIO_FOLDER, lang)
    os.makedirs(lang_dir, exist_ok=True)
    for mp3_id in df[df['lang'] == lang]['id']:
        source_file = os.path.join(AUDIO_FOLDER, f"{mp3_id}.mp3")
        destination_file = os.path.join(lang_dir, f"{mp3_id}.mp3")
        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
print("Files sorted by language.")

# -----------------------------------------------------
# PART 3: AUDIO PROCESSING AND CONCATENATION
# -----------------------------------------------------
print("\n### STEP 3: PROCESSING AND CONCATENATING AUDIO ###")

# Process and Concatenate Audio (Skip if Diarization Results Exist)
mapping_by_lang = {}  # Maps language code to list of (start, end, original filename)
if any(file.startswith("diarization_results_") for file in os.listdir(OUTPUT_BASE_FOLDER)):
    print("Diarization results already exist. Skipping audio processing and concatenation.")
else:
    for lang_folder in os.listdir(AUDIO_FOLDER):
        lang_path = os.path.join(AUDIO_FOLDER, lang_folder)
        if not os.path.isdir(lang_path):
            continue
        print(f"Processing language: {lang_folder}")
        temp_dir = tempfile.mkdtemp()
        extracted_files = []
        mapping = []  # For tracking segments: (start_time, end_time, original filename)
        current_time = 0.0
        silence_duration = 0.0
        if os.path.exists(SILENCE_FILE):
            try:
                silence_audio = AudioSegment.from_file(SILENCE_FILE)
                silence_duration = len(silence_audio) / 1000.0
            except:
                silence_duration = 0.0
        for filename in sorted(os.listdir(lang_path)):
            if filename.endswith(".mp3"):
                file_path = os.path.join(lang_path, filename)
                try:
                    audio = AudioSegment.from_file(file_path)
                except:
                    continue
                duration = len(audio) / 1000.0
                start_time = max(0, (duration / 2) - 5)
                extracted_file = os.path.join(temp_dir, f"extracted_{filename}")
                # Extract a 10-second segment
                audio[start_time * 1000:(start_time + 10) * 1000].export(extracted_file, format="mp3", bitrate="128k")
                extracted_files.append(f"file '{extracted_file}'")
                # Record mapping for this segment
                segment_duration = 10.0
                mapping.append((current_time, current_time + segment_duration, filename))
                current_time += segment_duration
                if os.path.exists(SILENCE_FILE):
                    extracted_files.append(f"file '{SILENCE_FILE}'")
                    current_time += silence_duration
        mapping_by_lang[lang_folder] = mapping
        if extracted_files:
            concat_list_file = os.path.join(temp_dir, "concat_list.txt")
            with open(concat_list_file, "w") as f:
                f.write("\n".join(extracted_files) + "\n")
            final_output = os.path.join(OUTPUT_BASE_FOLDER, f"final_output_{lang_folder}.mp3")
            subprocess.run(["ffmpeg", "-safe", "0", "-f", "concat", "-i", concat_list_file, "-c:a", "libmp3lame", "-b:a", "128k", final_output],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.rmtree(temp_dir)
print("Audio processing and concatenation completed.")

# -----------------------------------------------------
# PART 4: SPEAKER DIARIZATION
# -----------------------------------------------------
print("\n### STEP 4: PERFORMING SPEAKER DIARIZATION ###")

# Speaker Diarization (Skip if Results Exist)
if all(os.path.exists(os.path.join(OUTPUT_BASE_FOLDER, f"diarization_results_{lang}.csv")) for lang in df['lang'].unique()):
    print("All diarization results already exist. Skipping diarization.")
else:
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipeline.to(device)

    for audio_file in sorted(os.listdir(OUTPUT_BASE_FOLDER)):
        if audio_file.startswith("final_output_") and audio_file.endswith(".mp3"):
            lang_code = audio_file.replace("final_output_", "").replace(".mp3", "")
            audio_path = os.path.join(OUTPUT_BASE_FOLDER, audio_file)
            diarization_output = os.path.join(OUTPUT_BASE_FOLDER, f"diarization_results_{lang_code}.csv")
            
            if os.path.exists(diarization_output):
                print(f"Diarization results for {lang_code} already exist. Skipping.")
                continue
                
            waveform, sample_rate = torchaudio.load(audio_path)
            with ProgressHook() as hook:
                diarization = pipeline({"waveform": waveform, "sample_rate": sample_rate}, hook=hook)
            # Get mapping for this language
            mapping = mapping_by_lang.get(lang_code, [])
            with open(diarization_output, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Start (s)', 'Stop (s)', 'Speaker', 'Original File'])
                for turn, _, speaker in diarization.itertracks(yield_label=True):
                    mid = (turn.start + turn.end) / 2.0
                    original_file = audio_file  # fallback
                    for seg_start, seg_end, orig_file in mapping:
                        if seg_start <= mid <= seg_end:
                            original_file = orig_file
                            break
                    writer.writerow([f"{turn.start:.1f}", f"{turn.end:.1f}", f"speaker_{speaker}", original_file])
            print(f"Diarization results saved to {diarization_output}")

print("Diarization completed.")

# -----------------------------------------------------
# PART 5: GENDER PREDICTION MODEL SETUP
# -----------------------------------------------------
print("\n### STEP 5: SETTING UP GENDER PREDICTION MODEL ###")

# Define model classes for gender prediction
class ModelHead(nn.Module):
    def __init__(self, config, num_labels):
        super().__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.dropout = nn.Dropout(config.final_dropout)
        self.out_proj = nn.Linear(config.hidden_size, num_labels)

    def forward(self, features, **kwargs):
        x = features
        x = self.dropout(x)
        x = self.dense(x)
        x = torch.tanh(x)
        x = self.dropout(x)
        x = self.out_proj(x)
        return x

class AgeGenderModel(Wav2Vec2PreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.wav2vec2 = Wav2Vec2Model(config)
        self.age = ModelHead(config, 1)
        self.gender = ModelHead(config, 3)
        self.init_weights()

    def forward(self, input_values):
        outputs = self.wav2vec2(input_values)
        hidden_states = outputs[0]
        hidden_states = torch.mean(hidden_states, dim=1)
        logits_age = self.age(hidden_states)
        logits_gender = torch.softmax(self.gender(hidden_states), dim=1)
        return hidden_states, logits_age, logits_gender

# Set up device for computation
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))

# -----------------------------------------------------
# PART 6: GENDER PREDICTION
# -----------------------------------------------------
print("\n### STEP 6: PREDICTING GENDER FOR AUDIO FILES ###")

# Gender prediction output file
gender_predictions_path = os.path.join(OUTPUT_BASE_FOLDER, "gender_predictions.csv")

# Skip if gender predictions already exist
if os.path.exists(gender_predictions_path):
    print(f"Gender predictions file already exists at {gender_predictions_path}. Skipping prediction.")
else:
    # Get list of all audio files
    audio_files = []
    for root, dirs, files in os.walk(AUDIO_FOLDER):
        for f in files:
            if f.endswith('.mp3'):
                audio_files.append(os.path.join(root, f))
    
    # Load model and processor
    model_name = 'audeering/wav2vec2-large-robust-24-ft-age-gender'
    token = "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"
    processor = Wav2Vec2Processor.from_pretrained(model_name, token=token)
    model = AgeGenderModel.from_pretrained(model_name, token=token).to(device)
    model = model.half()

    def process_func(x: np.ndarray, sampling_rate: int, embeddings: bool = False) -> np.ndarray:
        y = processor(x, sampling_rate=sampling_rate)
        y = y['input_values'][0]
        y = y.reshape(1, -1)
        y = torch.from_numpy(y).to(device)
        y = y.half()
        with torch.no_grad():
            y = model(y)
            if embeddings:
                y = y[0]
            else:
                y = torch.hstack([y[1], y[2]])
        y = y.detach().cpu().numpy()
        return y

    def pad_segment(segment, min_length=16000):
        if len(segment) < min_length:
            padding = np.zeros(min_length - len(segment), dtype=segment.dtype)
            segment = np.concatenate((segment, padding))
        return segment

    def segment_signal(signal, segment_length=16000*30):
        return [signal[i:i + segment_length] for i in range(0, len(signal), segment_length)]

    def process_audio_file(file_path, target_sampling_rate=16000):
        waveform, original_sampling_rate = torchaudio.load(file_path)
        if original_sampling_rate != target_sampling_rate:
            resampler = Resample(orig_freq=original_sampling_rate, new_freq=target_sampling_rate)
            waveform = resampler(waveform)
        signal = waveform.numpy()[0]
        segments = segment_signal(signal, segment_length=16000*30)
        predictions = []
        for segment in segments:
            segment = pad_segment(segment, min_length=16000)
            prediction = process_func(segment, target_sampling_rate)
            gender = 'male' if np.argmax(prediction[0, 1:3]) == 1 else 'female'
            predictions.append(gender)
        final_gender = max(set(predictions), key=predictions.count)
        return final_gender

    # Process each audio file
    with open(gender_predictions_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Filename', 'Gender'])
        for i, audio_file in enumerate(audio_files):
            #print(f"Processing file {i+1}/{len(audio_files)}: {os.path.basename(audio_file)}")
            gender = process_audio_file(audio_file)
            writer.writerow([audio_file, gender])
            torch.cuda.empty_cache()

    print(f"Gender predictions saved to {gender_predictions_path}")

# -----------------------------------------------------
# PART 7: DATA PROCESSING AND OUTPUT
# -----------------------------------------------------
print("\n### STEP 7: PROCESSING DIARIZATION RESULTS AND CREATING OUTPUT FILES ###")

def process_diarization_results(gender_predictions_path, diarization_folder):
    # Load gender predictions file
    gender_predictions = pd.read_csv(gender_predictions_path)
    
    # Extract text ID from Filename column
    gender_predictions['TEXT_ID'] = gender_predictions['Filename'].apply(lambda x: os.path.splitext(os.path.basename(x))[0])
    
    # Create a dictionary for quick gender lookup
    gender_dict = dict(zip(gender_predictions['TEXT_ID'], gender_predictions['Gender']))
    
    # Process all diarization result files
    diarization_files = glob.glob(os.path.join(diarization_folder, "diarization_results_*.csv"))
    results = []
    
    for diarization_file in diarization_files:
        # Extract language code from filename
        lang_code = diarization_file.split('_')[-1].split('.')[0].upper()
        
        # Load diarization results
        diarization_results = pd.read_csv(diarization_file)
        
        # Ensure the correct column exists
        if "Original File" not in diarization_results.columns:
            continue
        
        # Extract text ID from "Original File" column
        diarization_results['TEXT_ID'] = diarization_results['Original File'].astype(str).str.replace('.mp3', '', regex=False)
        
        # Filter out non-numeric TEXT_ID values
        diarization_results = diarization_results[diarization_results['TEXT_ID'].str.isnumeric()]
        
        # Create speaker mappings
        speaker_mapping = {}
        for text_id, group in diarization_results.groupby('TEXT_ID'):
            speaker_counts = Counter(group['Speaker'])
            max_occurrences = max(speaker_counts.values(), default=0)
            
            if max_occurrences == 0:
                continue
                
            # Get speakers with max occurrences
            candidates = [speaker for speaker, count in speaker_counts.items() if count == max_occurrences]
            
            # Pick one randomly if there are ties
            selected_speaker = random.choice(candidates)
            
            # Rename the speaker based on language code
            speaker_code = f"{lang_code}{selected_speaker.split('_')[-1]}"
            
            # Store the mapping
            speaker_mapping[text_id] = speaker_code
        
        # Generate output with genders
        for text_id, speaker in speaker_mapping.items():
            gender = gender_dict.get(text_id, "Unknown")  # Default to "Unknown" if not found
            results.append([text_id, speaker, gender])
    
    # Convert to DataFrame and return
    return pd.DataFrame(results, columns=["TEXT_ID", "Speaker", "Gender"])

def create_interpreters_dataframe(output_df, texts_df):
    # Identify ST/SP texts that should not have interpreters assigned
    st_sp_texts = texts_df[(texts_df['source_target'] == "ST") & (texts_df['spoken_written'] == "SP")]
    st_sp_text_ids = set(st_sp_texts['id'].astype(str))
    
    # Remove speakers associated with ST/SP texts from the output dataframe
    filtered_output_df = output_df[~output_df['TEXT_ID'].isin(st_sp_text_ids)]
    
    # Get unique speakers
    unique_speakers = filtered_output_df[['Speaker', 'Gender']].drop_duplicates().reset_index(drop=True)
    
    # Add required columns
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    unique_speakers.rename(columns={'Speaker': 'interpreters.nickname', 'Gender': 'interpreters.gender'}, inplace=True)
    unique_speakers['interpreters.gender'] = unique_speakers['interpreters.gender'].replace({"male": "M", "female": "F"})
    unique_speakers['interpreters.native'] = "NA"
    unique_speakers['interpreters.created'] = now
    unique_speakers['interpreters.modified'] = now
    unique_speakers['interpreters.user_id'] = 25
    unique_speakers['interpreters.recycled'] = 0
    
    # Assign consecutive IDs starting from 1
    unique_speakers.insert(0, 'interpreters.id', range(1, len(unique_speakers) + 1))
    
    return unique_speakers

def update_texts_dataframe(texts_df, output_df, interpreters_df):
    # Ensure TEXT_ID and id columns are strings for proper mapping
    texts_df['id'] = texts_df['id'].astype(str)
    output_df['TEXT_ID'] = output_df['TEXT_ID'].astype(str)
    
    # Identify the texts that should not have an interpreter assigned
    st_sp_texts = texts_df[(texts_df['source_target'] == "ST") & (texts_df['spoken_written'] == "SP")]
    st_sp_text_ids = set(st_sp_texts['id'].astype(str))
    
    # Filter out ST/SP texts from the mapping process
    filtered_output_df = output_df[~output_df['TEXT_ID'].isin(st_sp_text_ids)]
    
    # Create a mapping of TEXT_ID to Speaker
    text_speaker_mapping = dict(zip(filtered_output_df['TEXT_ID'], filtered_output_df['Speaker']))
    
    # Create a mapping of Speaker to interpreter ID
    speaker_to_id = dict(zip(interpreters_df['interpreters.nickname'], interpreters_df['interpreters.id']))
    
    # Set all interpreter IDs to None first
    texts_df['texts.interpreter_id'] = None
    
    # Assign interpreter IDs to valid texts
    for text_id in texts_df['id'].unique():
        # Skip ST/SP texts
        if text_id in st_sp_text_ids:
            continue
            
        # Get the speaker for this text
        speaker = text_speaker_mapping.get(text_id)
        if speaker:
            # Get the interpreter ID for this speaker
            interpreter_id = speaker_to_id.get(speaker)
            if interpreter_id:
                texts_df.loc[texts_df['id'] == text_id, 'texts.interpreter_id'] = interpreter_id
    
    return texts_df

# Process the diarization results
output_df = process_diarization_results(gender_predictions_path, OUTPUT_BASE_FOLDER)

# Create interpreters dataframe with IDs properly assigned (after filtering out unwanted speakers)
interpreters_df = create_interpreters_dataframe(output_df, df)

# Update texts dataframe
texts_updated_df = update_texts_dataframe(df, output_df, interpreters_df)

# -----------------------------------------------------
# PART 8: SAVE OUTPUT AND CLEANUP
# -----------------------------------------------------
print("\n### STEP 8: SAVING OUTPUT FILES AND CLEANING UP ###")

# Save the final files
interpreters_updated_file_path = os.path.join(OUTPUT_BASE_FOLDER, "interpreters_new.xlsx")
texts_updated_file_path = os.path.join(OUTPUT_BASE_FOLDER, "texts_new.xlsx")
interpreters_df.to_excel(interpreters_updated_file_path, index=False)
texts_updated_df.to_excel(texts_updated_file_path, index=False)

print(f"Interpreters data saved to {interpreters_updated_file_path}")
print(f"Texts data saved to {texts_updated_file_path}")

# Cleanup intermediate files (keep only audio folders and final outputs)
for file in os.listdir(OUTPUT_BASE_FOLDER):
    file_path = os.path.join(OUTPUT_BASE_FOLDER, file)
    if file.startswith("final_output_") or file.startswith("diarization_results_") or file == "gender_predictions.csv":
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Removed intermediate file: {file}")

print("\n### PROCESSING COMPLETE ###")
print(f"Final output files: \n1. {texts_updated_file_path} \n2. {interpreters_updated_file_path}")
print("Audio folders and extracted audio files have been preserved.")