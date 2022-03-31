import zipfile
import pathlib
import os
import sys

dict = pathlib.Path("./temp")

with zipfile.ZipFile("test.epub","w",zipfile.ZIP_STORED) as archive:
    for file_path in dict.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(dict))

with zipfile.ZipFile("test.epub", mode="r") as archive:
    archive.printdir()