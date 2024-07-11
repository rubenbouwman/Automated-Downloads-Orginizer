import os

# File path for the folder that needs to be organized
filePath = r"C:/Users/ubrub/Downloads"

# Categories for the folders and their coresponding file types
categories = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# check if category folders exist, make the folder if it doesn't
for folder in categories:
    folderPath = os.path.join(filePath, folder)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

# Make a list of all the files in the given directory
fileList = [files for files in os.listdir(filePath)]


