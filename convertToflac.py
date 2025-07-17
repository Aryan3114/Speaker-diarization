import tarfile
import os

# Path to your downloaded .tar.gz
tar_path = "dev-clean.tar.gz"

# Folder to extract into
extract_folder = "LibriSpeech"

# Extract
with tarfile.open(tar_path, "r:gz") as tar:
    tar.extractall(path=extract_folder)

print("✅ Extraction complete!")
