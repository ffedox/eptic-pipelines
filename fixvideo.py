import os
import re

# Directories
pos_tagged_files_dir = "/home/afedotova/EPTIC25/eptic.v3/4. pos_tagged_files"
video_dir = "/home/afedotova/EPTIC25/eptic.v3/video"

# Ensure video directory exists
if not os.path.exists(video_dir):
    print(f"Video directory {video_dir} does not exist.")
    exit(1)

# Get list of video files with their extensions
video_files = {}
for f in os.listdir(video_dir):
    if os.path.isfile(os.path.join(video_dir, f)):
        name, ext = os.path.splitext(f)
        video_files[name] = ext  # Map video ID (name without extension) to its extension

# Iterate through .vert files
for root, _, files in os.walk(pos_tagged_files_dir):
    for file in files:
        if file.endswith(".vert"):
            file_path = os.path.join(root, file)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace video.php?id=NUM with NUM.<correct_extension>
            def replace_video_link(match):
                video_id = match.group(1)
                if video_id in video_files:
                    return f'video.php?id={video_id}{video_files[video_id]}'
                return match.group(0)  # No replacement if no match found
            
            updated_content = re.sub(
                r'video\.php\?id=(\d+)', 
                replace_video_link, 
                content
            )

            # Write changes back to the file if content was modified
            if updated_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated file: {file_path}")
