# --------------------------- Imports ---------------------------
import os
import shutil

# --------------------------- Setup ---------------------------
# File path for the folder that needs to be organized
# filePath = r"C:/Users/ubrub/Downloads"
filePath = input("Enter the path to Downloads folder: ")
fileList = []

# Categories for the folders and their coresponding file types
# New Categories and extensions can be added here
categories = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe'],
    'Folders':[],
    'Other':[]
}

# --------------------------- Functions ---------------------------
# Function to make a list of all the files in the given directory
def setFileList():
    global fileList
    print("Scanning files...")
    fileList = [files for files in os.listdir(filePath)]
    print(f"{len(fileList)} files found")

# check if category folders exist, make the folder if it doesn't
def makeFolders():
    for folder in categories:
        folderPath = os.path.join(filePath, folder)
        if not os.path.exists(folderPath):
            print(f"Making {folder} folder")
            os.makedirs(folderPath)

# Function to determine the category based on the file extension
def getCategory(file):
    if os.path.isdir(os.path.join(filePath, file)):
        return 'Folders'

    fileNames_Splitted = os.path.splitext(file)
    fileExtension = fileNames_Splitted[1].lower()
    for catagory, extensions in categories.items():
        if fileExtension in extensions:
            return catagory
    return "Other"

# Function to move a file to a category folder
def moveFile():
    print("Organizing...")
    for file in fileList:
        category = getCategory(file)
        fileSourcePath = os.path.join(filePath, file)
        destinationPath = os.path.join(filePath, category, file)
        shutil.move(fileSourcePath, destinationPath)
        print(f"Moved {file} to the {category} folder")

# Template method - Organize files to their respective folders
def run():
    setFileList()
    makeFolders()
    moveFile()
    print("Finished organizing!")

# --------------------------- Execute ---------------------------
run()
