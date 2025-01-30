import sys
import os
import torch
import pandas as pd
from glob import glob
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from CrisperWhisper.utils import adjust_pauses_for_hf_pipeline_output
import json

# Environment variable for CUDA module loading
os.environ["CUDA_MODULE_LOADING"] = "LAZY"

# Add CrisperWhisper directory to Python path
sys.path.append(os.path.abspath("/home/afedotova/EPTIC25/pipelines/CrisperWhisper"))

# Paths
xlsx_path = "/home/afedotova/EPTIC25/eptic.v4/1. database_tables/texts_for_test.xlsx"
audio_folder = "/home/afedotova/EPTIC25/eptic.v4/2. extracted_audios"
output_folder = "/home/afedotova/EPTIC25/eptic.v4/3. output_transcriptions"

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
        attn_implementation="eager",  # Keep this setting
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
        batch_size=2,
        return_timestamps="word",
        torch_dtype=torch.float16,
        device="cuda:0",
    )
except Exception as e:
    print(f"Error initializing model or pipeline: {e}")

# Load the Excel file
df = pd.read_excel(xlsx_path)

# Process all .wav files in extracted_audios directory
wav_files = glob(os.path.join(audio_folder, "*.wav"))

for wav_file in wav_files:
    video_id = os.path.splitext(os.path.basename(wav_file))[0]  # Extract ID from filename
    print(f"Processing audio: {wav_file}")

    # Load audio using librosa
    try:
        audio, sr = librosa.load(wav_file, sr=16000)  # Ensure correct sample rate

        # Transcribe the audio
        hf_pipeline_output = pipe(audio)
        
        # Adjust pauses (assuming adjust_pauses_for_hf_pipeline_output function exists)
        crisper_whisper_result = adjust_pauses_for_hf_pipeline_output(hf_pipeline_output)

        # Save the transcription
        output_file = os.path.join(output_folder, f"{video_id}_transcription.json")
        with open(output_file, "w") as file:
            json.dump(crisper_whisper_result, file, indent=4)

        print(f"Transcription saved to {output_file}")

    except Exception as e:
        print(f"Error processing audio {wav_file}: {e}")
