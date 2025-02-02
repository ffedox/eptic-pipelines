import os
import re

# Directory containing .vert files
directory = "/home/afedotova/EPTIC25/eptic.v3/4. pos_tagged_files"

# Regex patterns and replacements
patterns = [
    (r"http://amelia\.sslmit\.unibo\.it/video/video\.php\?id=", "https://media.dipintra.it/?id="),
    (r"\.wmv&|\.mp4&", "&"),
    (r"start=00\.(\d{2}\.\d{2})", r"start=\1"),
    (r"&end=00\.", "&end="),
    (r'(\d+)">', r'\1&collection=eptic3">')
]

# Process each .vert file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".vert"):
        filepath = os.path.join(directory, filename)

        # Read file content
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Apply regex replacements
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)

        # Write back modified content
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)