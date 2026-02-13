import os
import shutil

# Folder You Want to organize
FOLDER_PATH = os.getcwd()  # Fixed typo from grtcwd()

# File type mapping: Maps Folder Name to List of Extensions
FILE_TYPE = {
    'Python_Scripts': ['.py'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.svg'],
    'Data': ['.csv', '.json']
}
 
# Create folders if they don't exist
for folder in FILE_TYPE:
    if not os.path.exists(os.path.join(FOLDER_PATH, folder)):
        os.mkdir(os.path.join(FOLDER_PATH, folder))

# Organize files
for file in os.listdir(FOLDER_PATH):
    # Skip directories and the script itself so it doesn't move itself!
    if os.path.isdir(file) or file == os.path.basename(__file__):
        continue
 
    # Get the file extension (e.g., '.py')
    ext = os.path.splitext(file)[1].lower()
 
    for folder, extensions in FILE_TYPE.items():
        if ext in extensions:
            source = os.path.join(FOLDER_PATH, file)
            destination = os.path.join(FOLDER_PATH, folder, file)
            
            shutil.move(source, destination)
            print(f"Moved: {file} -> {folder}/")
            break
print("FILE ORGNIZE SUCCESFULLY✅")