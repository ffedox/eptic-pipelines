import os
import subprocess

# Define the directory containing the .txt files
directory = '/var/lib/manatee/utils/aligns'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Construct the full path of the file
        filepath = os.path.join(directory, filename)
        
        # Define the modifications to the filename
        new_filename = filename.replace('-eptic_', '.').replace('-ids', '').replace('eptic_', 'alignment.')
        new_filepath = os.path.join(directory, new_filename)
        
        # Use str.format for compatibility with Python versions earlier than 3.6
        command = 'python fixgaps.py < "{0}" > "{1}"'.format(filepath, new_filepath)
        subprocess.call(command, shell=True)

        # Check if the new filename is different from the original filename
        if new_filename != filename:
            # Remove the original file
            os.remove(filepath)
