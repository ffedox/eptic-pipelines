import sys
import os
import torch
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# Add CrisperWhisper directory to Python path
sys.path.append(os.path.abspath("/home/afedotova/EPTIC25/pipelines/CrisperWhisper"))
from utils import adjust_pauses_for_hf_pipeline_output

# Device and model settings
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "nyrahealth/CrisperWhisper"

# Load model and processor
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id,
    torch_dtype=torch_dtype,
    low_cpu_mem_usage=True,
    use_safetensors=True,
    use_auth_token="hf_XXXXXXXXXXXXXXXXXXXXXXXXXX",
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id, use_auth_token="hf_XXXXXXXXXXXXXXXXXXXXXXXXXX")

# Initialize the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    chunk_length_s=10,
    batch_size=4,
    return_timestamps='word',
    torch_dtype=torch_dtype,
    device=device,
)

# File path for transcription
audio_file_path = "/home/afedotova/EPTIC25/eptic25_v2/video/2098.wmv"
output_txt_path = "/home/afedotova/EPTIC25/eptic25_v2/video/2098_transcription.txt"

# Load audio
audio, sr = librosa.load(audio_file_path, sr=16000)  # Resample to 16kHz as required by most ASR models

# Transcribe the audio
hf_pipeline_output = pipe(audio)
crisper_whisper_result = adjust_pauses_for_hf_pipeline_output(hf_pipeline_output)

import json

output_dir = "/home/afedotova/EPTIC25/eptic25_v2/1. database_tables"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

output_txt_path = os.path.join(output_dir, "transcription.json")

with open(output_txt_path, "w") as file:
    json.dump(crisper_whisper_result, file, indent=4)

print(f"Transcription saved to {output_txt_path}")