# edited v5.5
import os

fileDir = os.getcwd()
allFile = os.listdir(fileDir)

files = []
directory = []
for dir in allFile:
    path = os.path.join(fileDir, dir)
    if os.path.isdir(path):
        directory.append(dir)

for file in allFile:
    path = os.path.join(fileDir, file)
    if file not in directory:
        files.append(file)

for file in files:
    path = os.path.join(fileDir, file)
    try:
        name, ext = file.split('.')
        if ext:
            w_dir = os.path.join(fileDir, ext)

            if ext not in directory:
                os.mkdir(w_dir)
                directory.append(ext)

            destination = os.path.join(fileDir, ext, file)
            os.rename(path, destination)

    except:
        print("error")
