import zipfile
import os
import sys

root = sys.path[0]
f = zipfile.ZipFile("test.epub","w",zipfile.ZIP_STORED)
dir = "./temp/"
for dirpath,dirnames,filenames in os.walk(dir):
    for filename in filenames:
        print(os.path.join(dirpath,filename))
        f.write(os.path.join(dirpath,filename))

f.close()
