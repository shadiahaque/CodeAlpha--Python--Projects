import os
import shutil
path = input("Enter folder path: ")
files = os.listdir(path)
for file in files:
    
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            folder = os.path.join(path, "Images")
        elif file.endswith(".pdf"):
            folder = os.path.join(path, "PDFs")
        elif file.endswith(".txt"):
            folder = os.path.join(path, "Text Files")
        else:
            folder = os.path.join(path, "Others")
        if not os.path.exists(folder):
            os.mkdir(folder)
        shutil.move(file_path, os.path.join(folder, file))
                    
print("Files organized successfully!")
