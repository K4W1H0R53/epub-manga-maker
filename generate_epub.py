import zipfile
import pathlib
import os
import sys

##
# os.system("zip -X0 ./test.epub ./temp/mimetype")
# os.system("zip -9 -r ./test.epub ./temp/META-INF ./temp/OEBPS")

dict = pathlib.Path("./temp")
with zipfile.ZipFile("test.epub","a",zipfile.ZIP_STORED) as archive:
    archive.writestr("mimetype", "application/epub+zip")
    for file_path in dict.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(dict))