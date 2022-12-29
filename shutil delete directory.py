import os
import shutil

path = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "OOOOOOO"

#os.mkdir(path)
try:
    shutil.rmtree(path)   # if exist remove folder
    os.mkdir(path)        # new folder
except:
    os.mkdir(path)
