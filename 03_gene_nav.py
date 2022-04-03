import os
import sys
import re

root = sys.path[0]
contents = []   ## 用于储存章节名
pages = []  ## 用于储存章节开始页文件名
landmarks = []   ## 用于储存landmark

with open("./contents_other.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()   ## 读取contents.txt文本文件，文本文件以"$章节名|$起始页文件名"的方式储存正文目录
    for i in contents_table:
        a = i.split('|',2)[0]
        b = i.split('|',2)[1]
        if i.find("#") != -1:    ## 跳过星标行
            continue
        if i.find("*") != -1:    ## 确认正文行
            contents.append(a)
            pages.append(b)
            landmarks.append("bodymatter")
            continue
        if i.find("cover") != -1:   ## 设置epub封面
            contents.append(a)
            pages.append(b)           
            landmarks.append("cover")
            continue
        if i.find("表纸") != -1 or i.find("封面") != -1:
            contents.append(a)
            pages.append(b)           
            landmarks.append("")
            continue        
        if i.find("目次")!= -1 or i.find("目錄")!= -1:
            contents.append(a)
            pages.append(b)
            landmarks.append("toc")
            continue
        if i.find("奥付")!= -1 or i.find("版權頁")!= -1:
            contents.append(a)
            pages.append(b)
            landmarks.append("colophon")
            continue
        else:
            contents.append(a)
            pages.append(b)
            landmarks.append("")

zipped_list = zip(landmarks,pages,contents)
total = list(zipped_list)
toc_list = []
landmarks_list = []
for x in total:
    if len(x[0]) != 0:
        landmarks_element = '''<li><a epub:type="{0}" href="Text/{1}.xhtml">{2}</a></li>'''.format(x[0],x[1],x[2])
        landmarks_list.append(landmarks_element)
    if x[2] == "cover":
        continue
    toc_element = '''<li><a href="Text/{0}.xhtml">{1}</a></li>'''.format(x[1],x[2])
    toc_list.append(toc_element)

f=open("./templates/nav_templates.xhtml",mode="r",encoding="utf-8")
f = f.read()

for a in toc_list:
    post = f.find("</ol>")
    f = f[:post] + a + "\r        "  + f[post:]
for b in landmarks_list:
    post1 = f.find("</ol>")
    post2 = f.find("</ol>", post1+1)
    f = f[:post2] + b + "\r        "  + f[post2:]

file = open("./temp/OEBPS/nav.xhtml",mode="w",encoding="utf-8")
file.write(f)
