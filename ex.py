import os
import zipfile

# Set the directory path containing the zip files
dir_path = '.'

# Loop through all files in the directory
for file_name in os.listdir(dir_path):
    # Check if the file is a zip file
    if file_name.endswith('.zip'):
        # Open the zip file
        with zipfile.ZipFile(os.path.join(dir_path, file_name), 'r') as zip_ref:
            # Extract all contents of the zip file to the directory
            zip_ref.extractall(dir_path)
