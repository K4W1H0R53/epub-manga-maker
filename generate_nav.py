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
        contents.append(a)
        pages.append(b)
        if i.find("#") != -1:    ## 跳过星标行
            print("跳过",i)
            continue
        if i.find("*") != -1:    ## 确认正文行
            content = [a,b,"bodymatter"]
            landmarks.append(content)
            print ("生成landmarks标签:",content)
        if i.find("cover") != -1:
            content = [a,b,"cover"]
            landmarks.append(content)
            print ("生成landmarks标签:",content)
        if i.find("目次")!= -1:
            content = [a,b,"toc"]
            landmarks.append(content)
            print ("生成landmarks标签:",content)
        if i.find("奥付")!= -1:
            content = [a,b,"colophon"]
            print ("生成landmarks标签:",content)
            landmarks.append(content)

print("章节表：",contents)
print("页数表：",pages)
print("landmark表：",landmarks)