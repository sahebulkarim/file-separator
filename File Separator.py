import os

def currentDirectory():
    print("Current working directory:", os.getcwd())

currentFilePath = currentDirectory()

# read the files from the folder
folderpath = r"C:\Users\CIRT-DF\Desktop\Case Files - simple"

def changeDirectory():
    # read the files from the folder
    folderpath = r"C:\Users\CIRT-DF\Desktop\Case Files - simple"
    os.chdir(folderpath)
    print("New directory:",os.getcwd())

newFilePath = changeDirectory()


def fileAndExtension():
    print("List of the file names:", os.listdir())

    list_extension = []
    for fl in os.listdir():
        extension = fl.split(".")[-1]  # -1 last element of the list
        list_extension.append(extension)

    list_extension = list(set(list_extension))  # Remove duplicate but garbage value remains
    print("List of the extensions:", list_extension)

    print(len(list_extension))

fileExtension = fileAndExtension()
