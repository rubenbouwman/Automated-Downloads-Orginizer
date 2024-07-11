# --------------------------- Imports ---------------------------
import os
import shutil

# --------------------------- Setup ---------------------------
# File path for the folder that needs to be organized
filePath = r"C:/Users/ubrub/Downloads/Testfolder"

# Categories for the folders and their coresponding file types
# New Categories and extensions can be added here
categories = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe']
}

# check if category folders exist, make the folder if it doesn't
for folder in categories:
    folderPath = os.path.join(filePath, folder)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

# Make a list of all the files in the given directory
fileList = [files for files in os.listdir(filePath)]

# --------------------------- Functions ---------------------------
# Function to determine the category based on the file extension
def getCategory(file):
    fileNames_Splitted = os.path.splitext(file)
    fileExtension = fileNames_Splitted[1].lower()
    for catagory, extensions in categories.items():
        if fileExtension in extensions:
            return catagory
    return None

# Function to move a file to a category folder
def moveFile(file, category):
    if category:
        fileSourcePath = os.path.join(filePath, file)
        destinationPath = os.path.join(filePath, category, file)
        shutil.move(fileSourcePath, destinationPath)
        print(f"Moved {file} to the {category} folder")

# --------------------------- Execute ---------------------------
# Organize files to their respective folders
for file in fileList:
    category = getCategory(file)
    print(f"moving {file} to {category}")
    moveFile(file, category)
