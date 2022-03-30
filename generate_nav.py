import os
import sys
import re

root = sys.path[0]
contents = []   ## 用于储存章节名
pages = []  ## 用于储存章节开始页文件名
landmarks = []   ## 用于储存landmark

with open(root+"/templates/contents.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()   ## 读取contents.txt文本文件，文本文件以"$章节名|$起始页文件名"的方式储存正文目录
    for i in contents_table:
        a = i.split('|',2)[0]
        b = i.split('|',2)[1]
        if i.find("#") != -1:    ## 跳过星标行
            # print("跳过",i)
            continue
        if i.find("*") != -1:    ## 确认正文行
            contents.append(a)
            pages.append(b)
            landmarks.append("bodymatter")
            # print ("生成landmarks标签:",[a,b,"bodymatter"])
            continue
        if i.find("cover") != -1:
            contents.append(a)
            pages.append(b)           
            landmarks.append("cover")
            # print ("生成landmarks标签:",[a,b,"cover"])
            continue
        if i.find("目次")!= -1:
            contents.append(a)
            pages.append(b)
            landmarks.append("toc")
            # print ("生成landmarks标签:",[a,b,"toc"])
            continue
        if i.find("奥付")!= -1:
            contents.append(a)
            pages.append(b)
            # print ("生成landmarks标签:",[a,b,"colophon"])
            landmarks.append("colophon")
            continue
        else:
            contents.append(a)
            pages.append(b)
            landmarks.append("")
            continue

zipped_list = zip(landmarks,pages,contents)
total = list(zipped_list)
f=open(root + "/templates/OEBPS/nav.xhtml",mode="r",encoding="utf-8")
f = f.read()
for x in total:
    if len(x[0]) != 0:
        c = '''<li><a epub:type="{0}" href="Text/{1}.xhtml">{2}</a></li>'''.format(x[0],x[1],x[2])
        print(c)