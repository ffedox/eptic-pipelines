from pyannote.audio import Pipeline
import torchaudio
from pyannote.audio.pipelines.utils.hook import ProgressHook
import torch
import csv

# Initialize the pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="hf_XXXXXXXXXXXXXXXXXXXXXXXXXX")

import logging

# Configure logging
logging.basicConfig(filename='my_diarization_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example of logging GPU or CPU usage
if torch.cuda.is_available():
    device = torch.device("cuda")
    logging.info(f"Using GPU: {torch.cuda.get_device_name(device)}")
else:
    device = torch.device("cpu")
    logging.info("Using CPU")

# send pipeline to GPU (when available)
pipeline.to(torch.device("cuda"))

# Pre-load your final output audio file into memory
waveform, sample_rate = torchaudio.load("/home/afedotova/whisperx/final_output_sl.mp3")
# Note: Ensure the audio format is supported by `torchaudio.load`. If your file is an MP3, you might need additional steps or libraries to handle it, as `torchaudio`'s support for MP3 can be limited depending on the backend.

# Monitoring progress
with ProgressHook() as hook:
    # Apply pretrained pipeline on your waveform loaded into memory 
    # Ensure to pass the loaded waveform and sample rate
    diarization = pipeline({"waveform": waveform, "sample_rate": sample_rate}, hook=hook)

# Load the clip timings for cross-referencing
clip_timings = []
with open("/home/afedotova/whisperx/clip_timings_sl.csv", mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    for row in reader:
        start, end, filename = row
        clip_timings.append((float(start), float(end), filename))

# Function to find the corresponding file for a given segment
def find_corresponding_file(middle_point):
    for start, end, filename in clip_timings:
        if start <= middle_point <= end:
            return filename
    return None

# Prepare to save the diarization results with original file mappings
csv_file = "/home/afedotova/whisperx/diarization_results_sl.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Start (s)', 'Stop (s)', 'Speaker', 'Original File'])

    # Process each diarization segment
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        # Calculate the middle point of the segment
        middle_point = (turn.start + turn.end) / 2
        # Find the original file corresponding to this middle point
        original_file = find_corresponding_file(middle_point)
        # Write the diarization result and corresponding original file to CSV
        writer.writerow([f"{turn.start:.1f}", f"{turn.end:.1f}", f"speaker_{speaker}", original_file])

print(f"Diarization results saved to {csv_file}")
