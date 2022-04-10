import get_metadate,os,sys,uuid,time,cv2
import numpy as np

path_image = os.walk("./temp/OEBPS/Images")
title = ['test','test']
for path, dirs, files in path_image:
    for file in files:
        img = cv2.imdecode(np.fromfile(os.path.join(path, file), dtype=np.uint8), 1)
        src_width = img.shape[1]
        src_height = img.shape[0]
        page_html = '''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">  <head>
            <meta charset="UTF-8"/>
            <title>{3}</title>
            <meta name="viewport" content="width={0}, height={1}" />
            </head>  <body style="margin:0;padding:0;">
            <div>
                <svg style="margin:0;padding:0;" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" viewBox="0 0 {0} {1}">
                <image width="{0}" height="{1}" xlink:href="../Images/{2}"/>
                </svg>
            </div>
            </body>
        </html>'''.format(src_width, src_height, file,title[0])
        f = open("./temp/OEBPS/Text/" + os.path.splitext(file)[0] + ".xhtml", mode="w", encoding="utf-8")
        f.write(page_html)