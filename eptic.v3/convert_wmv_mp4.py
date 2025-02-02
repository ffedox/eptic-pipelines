import os
import subprocess

# Directory containing .wmv files
video_dir = "/home/afedotova/EPTIC25/eptic.v3/video"
output_log = os.path.join(video_dir, "converted_files.txt")

# List to store converted file names
converted_files = []

# Iterate through all .wmv files in the directory
for filename in os.listdir(video_dir):
    if filename.endswith(".wmv"):
        input_path = os.path.join(video_dir, filename)
        output_path = os.path.join(video_dir, filename.replace(".wmv", ".mp4"))

        # ffmpeg command
        command = [
            "ffmpeg", "-i", input_path, "-c:v", "libx264", "-crf", "23",
            "-preset", "fast", "-c:a", "aac", "-b:a", "128k", output_path
        ]

        # Execute conversion
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Add to converted files list
        converted_files.append(filename)

# Save list of converted files to a text file
with open(output_log, "w", encoding="utf-8") as log_file:
    for file in converted_files:
        log_file.write(file + "\n")