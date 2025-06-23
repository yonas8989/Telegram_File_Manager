import os
import shutil

# Define the download directory (adjust for your system)
download_dir = r"C:\Users\hp\Downloads\telegram Desktop"  # Linux/macOS path
# For Windows, use: download_dir = r"C:\download\telegram download"

# Define file categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
    "Others": []  # For uncategorized files
}

# Create subfolders if they don't exist
for category in file_categories:
    category_path = os.path.join(download_dir, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Iterate through files in the download directory
for filename in os.listdir(download_dir):
    file_path = os.path.join(download_dir, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Get file extension
    file_ext = os.path.splitext(filename)[1].lower()
    
    # Find matching category
    moved = False
    for category, extensions in file_categories.items():
        if file_ext in extensions:
            destination = os.path.join(download_dir, category, filename)
            try:
                shutil.move(file_path, destination)
                print(f"Moved {filename} to {category}")
                moved = True
            except Exception as e:
                print(f"Error moving {filename}: {e}")
            break
    
    # Move to 'Others' if no category matches
    if not moved:
        destination = os.path.join(download_dir, "Others", filename)
        try:
            shutil.move(file_path, destination)
            print(f"Moved {filename} to Others")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

print("File organization complete!")