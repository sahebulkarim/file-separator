import os
import shutil

def currentDirectory():
    print("Current working directory:", os.getcwd())

currentFilePath = currentDirectory()

# read the files from the folder
#folderpath = r"C:\Users\CIRT-DF\Desktop\Case Files - simple"

def changeDirectory():
    # read the files from the folder
    folderpath = r"C:\Users\CIRT-DF\Desktop\Test Files for File Separator - Copy"
    os.chdir(folderpath)
    print("New directory:",os.getcwd())

newFilePath = changeDirectory()


# List down file names
print("List of the file names:", os.listdir())

list_extension = []
for fl in os.listdir():
    extension = fl.split(".")[-1]  # -1 last element of the list
    list_extension.append(extension)

list_extension = list(set(list_extension))  # Remove duplicate but garbage value remains
print("List of the extensions:", list_extension)

print(len(list_extension))


path = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "File_Separated"
os.mkdir(path)
print(path)

for ex in list_extension:
    print(ex,end=",")
    os.mkdir(path + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl,path + "\\" + ex)

