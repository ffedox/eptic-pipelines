import os
import tqdm
import torch
import torchaudio
import numpy as np
import pandas as pd
from torch import nn
from torch.utils.data import DataLoader
from torch.nn import functional as F
import torchaudio
from torchaudio.transforms import Resample
import soundfile as sf
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification, Wav2Vec2Processor

import os
import subprocess

# Define the directory path
directory_path = '/home/afedotova/noskeptic/video/all'

# List all .mp4 and .wmv files in the directory
# Create a directory for the extracted audio files

# List all extracted .mp3 files with their absolute paths
extracted_audio_dir = "/home/afedotova/noskeptic/video/all/extracted_audio"
audio_files = [os.path.join(extracted_audio_dir, f) for f in os.listdir(extracted_audio_dir) if os.path.isfile(os.path.join(extracted_audio_dir, f))]

import numpy as np
import torch
import torch.nn as nn
from transformers import Wav2Vec2Processor
from transformers.models.wav2vec2.modeling_wav2vec2 import (
    Wav2Vec2Model,
    Wav2Vec2PreTrainedModel,
)


class ModelHead(nn.Module):
    r"""Classification head."""

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
    r"""Speech emotion classifier."""

    def __init__(self, config):

        super().__init__(config)

        self.config = config
        self.wav2vec2 = Wav2Vec2Model(config)
        self.age = ModelHead(config, 1)
        self.gender = ModelHead(config, 3)
        self.init_weights()

    def forward(
            self,
            input_values,
    ):

        outputs = self.wav2vec2(input_values)
        hidden_states = outputs[0]
        hidden_states = torch.mean(hidden_states, dim=1)
        logits_age = self.age(hidden_states)
        logits_gender = torch.softmax(self.gender(hidden_states), dim=1)

        return hidden_states, logits_age, logits_gender


def process_func(x: np.ndarray, sampling_rate: int, embeddings: bool = False) -> np.ndarray:
    # run through processor to normalize signal
    y = processor(x, sampling_rate=sampling_rate)
    y = y['input_values'][0]
    y = y.reshape(1, -1)
    y = torch.from_numpy(y).to(device)

    # Convert input to half precision to match the model
    y = y.half()

    # run through model
    with torch.no_grad():
        y = model(y)
        if embeddings:
            y = y[0]
        else:
            y = torch.hstack([y[1], y[2]])

    # convert to numpy
    y = y.detach().cpu().numpy()

    return y

print(torch.cuda.is_available())

import numpy as np
import torch
import torch.nn as nn
import soundfile as sf
from transformers import Wav2Vec2Processor
from transformers.models.wav2vec2.modeling_wav2vec2 import (
    Wav2Vec2Model,
    Wav2Vec2PreTrainedModel,
)
import csv

# Assuming model and processor are loaded as shown in your snippet
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# If CUDA (GPU) is available, it will also print the name of the GPU
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))

model_name = 'audeering/wav2vec2-large-robust-24-ft-age-gender'
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = AgeGenderModel.from_pretrained(model_name).to(device)
model = model.half()  # Convert model to use FP16

# Your list of audio file paths
audio_files = audio_files

def pad_segment(segment, min_length=16000):
    """Pad the segment to a minimum length with zeros."""
    if len(segment) < min_length:
        padding = np.zeros(min_length - len(segment), dtype=segment.dtype)
        segment = np.concatenate((segment, padding))
    return segment

def segment_signal(signal, segment_length=16000*30):  # 30 seconds segments
    """Segments the signal into smaller chunks of segment_length."""
    return [signal[i:i + segment_length] for i in range(0, len(signal), segment_length)]


def process_audio_file(file_path, target_sampling_rate=16000):
    # Load and resample the audio file, similar to previous steps
    waveform, original_sampling_rate = torchaudio.load(file_path)
    if original_sampling_rate != target_sampling_rate:
        resampler = Resample(orig_freq=original_sampling_rate, new_freq=target_sampling_rate)
        waveform = resampler(waveform)
    signal = waveform.numpy()[0]
    
    # Segment the signal into smaller chunks
    segments = segment_signal(signal, segment_length=16000*30)  # Example: 30-second segments

    predictions = []
    for segment in segments:
        # Ensure the segment meets the minimum length required by the model
        segment = pad_segment(segment, min_length=16000)  # Adjust min_length as needed

        prediction = process_func(segment, target_sampling_rate)
        gender = 'male' if np.argmax(prediction[0, 1:3]) == 1 else 'female'
        predictions.append(gender)

    # Aggregate predictions
    final_gender = max(set(predictions), key=predictions.count)
    return final_gender


# Prepare to write results to CSV
csv_file = 'gender_predictions.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Gender'])
    
    for audio_file in audio_files:
        gender = process_audio_file(audio_file)
        writer.writerow([audio_file, gender])
        torch.cuda.empty_cache()  # Free up unused memory after each file

print(f"Predictions saved to {csv_file}.")