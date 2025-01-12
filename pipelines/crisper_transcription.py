import sys
import os
import torch
import pandas as pd
from glob import glob
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import json

import os
os.environ["CUDA_MODULE_LOADING"] = "LAZY"

# Add CrisperWhisper directory to Python path
sys.path.append(os.path.abspath("/home/afedotova/EPTIC25/pipelines/CrisperWhisper"))

# Paths
xlsx_path = "/home/afedotova/EPTIC25/eptic.v4/1. database_tables/texts_for_test.xlsx"
video_folder = "/home/afedotova/EPTIC25/eptic.v4/video"
output_folder = "/home/afedotova/EPTIC25/eptic.v4/output_transcriptions"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

if not torch.cuda.is_available():
    raise RuntimeError("CUDA is not available. Check your GPU setup.")
else:
    print(f"Using device: {torch.cuda.get_device_name(0)}")

# Device and model settings
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "nyrahealth/CrisperWhisper"

processor = AutoProcessor.from_pretrained(model_id, use_auth_token="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")

try:
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
        use_safetensors=True,
        attn_implementation="eager",  # Add this argument
        token="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",
    )
    model.to("cuda:0")
    torch.cuda.empty_cache()

    processor = AutoProcessor.from_pretrained(model_id, token="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")
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=10,
        batch_size=4,
        return_timestamps='word',
        torch_dtype=torch.float16,
        device="cuda:0",
    )
except Exception as e:
    print(f"Error initializing model or pipeline: {e}")


# Load the Excel file
df = pd.read_excel(xlsx_path)

# Iterate over rows where texts.plain_text is empty
for index, row in df[df['texts.plain_text'].isna()].iterrows():
    video_id = row['id']
    
    # Find the video file with matching ID, ignoring extension
    video_files = glob(os.path.join(video_folder, f"{video_id}.*"))  # Match any file extension
    if video_files:
        video_path = '/home/afedotova/EPTIC25/eptic.v4/video/1855.mp3'  # Use the first match
        print(f"Processing video: {video_path}")

        # Load audio from video (using librosa for simplicity)
        try:
            audio, sr = librosa.load(video_path, sr=16000)  # Resample to 16kHz as required by most ASR models

            # Transcribe the audio
            hf_pipeline_output = pipe(audio)
            crisper_whisper_result = adjust_pauses_for_hf_pipeline_output(hf_pipeline_output)

            # Save the transcription
            output_file = os.path.join(output_folder, f"{video_id}_transcription.json")
            with open(output_file, "w") as file:
                json.dump(crisper_whisper_result, file, indent=4)

            print(f"Transcription saved to {output_file}")

        except Exception as e:
            print(f"Error processing video {video_path}: {e}")
    else:
        print(f"Video file not found for ID: {video_id}")

