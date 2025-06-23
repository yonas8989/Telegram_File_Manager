import os
import shutil
from datetime import datetime  # Add this import

# Define the download directory
download_dir = r"C:\Users\hp\Downloads\telegram Desktop"

# Verify the directory exists
if not os.path.exists(download_dir):
    print(f"Error: The directory {download_dir} does not exist. Please check the path.")
    exit()

print(f"Scanning directory: {download_dir}")
print(f"Files found: {os.listdir(download_dir)}")

# Define file categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
    "Others": []
}

# Create subfolders with date (e.g., 2025-06)
date_folder = datetime.now().strftime("%Y-%m")  # e.g., 2025-06
for category in file_categories:
    category_path = os.path.join(download_dir, category, date_folder)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
        print(f"Created folder: {category_path}")

# Function to handle duplicate filenames
def get_unique_destination(destination):
    base, ext = os.path.splitext(destination)
    counter = 1
    while os.path.exists(destination):
        destination = f"{base}({counter}){ext}"
        counter += 1
    return destination

# Counter for moved files
moved_count = 0

# Iterate through files in the download directory
for filename in os.listdir(download_dir):
    file_path = os.path.join(download_dir, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        print(f"Skipping directory: {filename}")
        continue
    
    # Get file extension
    file_ext = os.path.splitext(filename)[1].lower()
    print(f"Processing file: {filename} (Extension: {file_ext})")
    
    # Find matching category
    moved = False
    for category, extensions in file_categories.items():
        if file_ext in extensions:
            destination = os.path.join(download_dir, category, date_folder, filename)  # Add date_folder
            destination = get_unique_destination(destination)
            try:
                shutil.move(file_path, destination)
                print(f"Moved {filename} to {category}/{date_folder}")
                moved_count += 1
                moved = True
            except Exception as e:
                print(f"Error moving {filename}: {e}")
            break
    
    # Move to 'Others' if no category matches
    if not moved and file_ext:
        destination = os.path.join(download_dir, "Others", date_folder, filename)
        destination = get_unique_destination(destination)
        try:
            shutil.move(file_path, destination)
            print(f"Moved {filename} to Others/{date_folder}")
            moved_count += 1
        except Exception as e:
            print(f"Error moving {filename}: {e}")

print(f"File organization complete! {moved_count} files moved.")