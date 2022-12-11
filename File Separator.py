import os

#fazlul's code
print("code added here")

# check current directory
print(os.getcwd())

# read the files from a folder
folderpath = r"C:\Users\CIRT\PycharmProjects\File Separator\Files"

# change directory to my files
os.chdir(folderpath)
print(os.getcwd())

# check files in the folder
print(os.listdir())

# get extension
list_extension = []
for f in os.listdir():
    extension = f.split(".")[-1]   # -1 last element of the list
    list_extension.append(extension)

print(list_extension)
