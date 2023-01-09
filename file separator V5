# edited v5
import os

wd = os.getcwd()
alll = os.listdir(wd)

files = []
dirs = []
for dirr in alll:
    path = os.path.join(wd, dirr)
    if os.path.isdir(path):
        dirs.append(dirr)

for file in alll:
    path = os.path.join(wd, file)
    if file not in dirs:
        files.append(file)

for file in files:
    path = os.path.join(wd, file)
    try:
        name, ext = file.split('.')
        if ext:
            w_dir = os.path.join(wd, ext)

            if ext not in dirs:
                os.mkdir(w_dir)
                dirs.append(ext)

            w_files = os.listdir(w_dir)
            suffix = ''
            i = 0;
            while file in w_files:
                i += 1
                suffix = '__' + 'i'
                file = name + suffix + "." + ext

            dest = os.path.join(wd, ext, file)
            os.rename(path, dest)
    except:
        print("error")


