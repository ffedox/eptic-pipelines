#!/usr/bin/env python3
"""
Script to process .pretgd files by applying a series of transformations
to clean up transcription features in the text content.
"""

import os
import re
import glob
import argparse
from pathlib import Path

def transform_text(text):
    """
    Apply transformations to clean up transcription features.
    This is a Python implementation of the Perl transform subroutine.
    """
    # Signal disfluencies
    text = re.sub(r'([a-zA-Z])- ', r'\1PIPPERO ', text)
    
    # Remove explicit markers of italics
    text = re.sub(r' ?#ie?# ?', ' ', text)
    
    # Remove tags like /.../
    text = re.sub(r'/(.+?)/', '', text)
    
    # Remove comments in [...] brackets
    text = re.sub(r'\[.+?\]', '', text)
    
    # Delete space before three dots
    text = re.sub(r' \.\.\.', '...', text)
    
    # Remove curly braces while keeping the content inside
    text = re.sub(r'[{}]+', '', text)
    
    return text

def process_file(file_path, backup=True):
    """
    Process a single .pretgd file, applying transformations to text content
    within <s> tags.
    
    Args:
        file_path: Path to the .pretgd file
        backup: If True, create a backup of the original file
    """
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if backup:
        # Create a backup of the original file
        backup_path = str(file_path) + '.bak'  # Convert Path to string before concatenating
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created backup: {backup_path}")
    
    # Define a pattern to find text within <s> tags
    s_tag_pattern = re.compile(r'(<s id="[^"]*"[^>]*>)\n(.*?)\n(</s>)', re.DOTALL)
    
    # Function to process each match
    def replace_match(match):
        s_open_tag = match.group(1)
        text = match.group(2)
        s_close_tag = match.group(3)
        
        # Apply transformations to the text
        transformed_text = transform_text(text)
        
        return f"{s_open_tag}\n{transformed_text}\n{s_close_tag}"
    
    # Apply transformations to all <s> tag contents
    modified_content = s_tag_pattern.sub(replace_match, content)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"Processed: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Transform PRETGD files to clean up transcription features.")
    parser.add_argument("--folder", default="/home/afedotova/EPTIC25/eptic.v4/3. pre_pos_files", 
                       help="Path to the folder containing .pretgd files")
    parser.add_argument("--backup", action="store_true", 
                       help="Create backup files (default: no backups)")
    
    args = parser.parse_args()
    
    # Ensure the folder path exists
    folder_path = Path(args.folder)
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: Folder '{args.folder}' does not exist or is not a directory.")
        return
    
    # Get all .pretgd files
    pretgd_files = list(folder_path.glob("*.pretgd"))
    
    if not pretgd_files:
        print(f"No .pretgd files found in {args.folder}")
        return
    
    print(f"Found {len(pretgd_files)} .pretgd files to process.")
    
    # Process each file
    for file_path in pretgd_files:
        process_file(file_path, backup=args.backup)
    
    print(f"All {len(pretgd_files)} files processed successfully.")

if __name__ == "__main__":
    main()