import os
import pandas as pd
import subprocess

# Paths
video_dir = "/home/afedotova/EPTIC25/eptic.v4/video"
xlsx_path = "/home/afedotova/EPTIC25/eptic.v4/1. database_tables/texts_for_test.xlsx"
output_dir = "/home/afedotova/EPTIC25/eptic.v4/2. extracted_audios"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load Excel file
df = pd.read_excel(xlsx_path, dtype={'id': str})  # Ensure 'id' is treated as a string

# Filter the dataframe
filtered_df = df[(df["spoken_written"] == "SP") & (df["texts.plain_text"].isna())]

# Process each matching video
for video_id in filtered_df["id"]:
    video_path = os.path.join(video_dir, f"{video_id}.mp4")
    audio_path = os.path.join(output_dir, f"{video_id}.wav")  # Change to WAV format

    if os.path.exists(video_path):
        command = [
            "ffmpeg",
            "-i", video_path,
            "-acodec", "pcm_s16le",  # WAV codec
            "-ar", "16000",  # Set sample rate to 16kHz (adjust if needed)
            "-ac", "1",  # Convert to mono
            "-y",  
            audio_path
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
