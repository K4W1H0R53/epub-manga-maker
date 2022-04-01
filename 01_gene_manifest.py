import os
import sys
import uuid
import time


path_image = os.walk("./books/test")
############################### 图片列表###############################
filename_list = []
extension_list = []
for path, dir_list, file_list in path_image:
    for index, file_name in enumerate(sorted(file_list)):
        filename = os.path.splitext(file_name)[0]
        extension = os.path.splitext(file_name)[1]
        filename_list.append(filename)
        extension_list.append(extension)
############################### 输入元数据###############################
isbn = input("输入ISBN:")
publisher = input("输入出版社名称(1.wani; 2.got; 3.core; 4.茜新社; 5.hit; 6.ktc; 7.kuroe; 8.mujin):")
if publisher == "1":
  publisher = "ワニマガジン社"
  print(publisher)
if publisher == "2":
  publisher = "GOT"
  print(publisher)
if publisher == "3":
  publisher = "コアマガジン"
  print(publisher)
if publisher == "4":
  publisher = "茜新社"
  print(publisher)
if publisher == "5":
  publisher = "ヒット出版社"
  print(publisher)
if publisher == "6":
  publisher = "KILL TIME COMMUNICATION"
  print(publisher)
if publisher == "7":
  publisher = "クロエ出版"
  print(publisher)
if publisher == "8":
  publisher = "ティーアイネット"
  print(publisher)
else:
  print(publisher)
publish_date = input("输入发售日期:")
author = input("输入作者名:")
title = input("输入作品名:")
language = input("输入语言(1.中文; 2.繁体中文; 3.日文):")
if language == "1":
  language = "zh-CN"
  print(language)
if language == "2":
  language = "zh-TW"
  print(language)
if language == "3":
  language = "ja"
  print(language)
source = input("输入图源类型(1.扫图; 2.Bookwalker; 3.DLsite; 4.KOBO; 5.PUBU):")
if source == "1":
  source = "SCAN"
  print(source)
if source == "2":
  source = "BOOKWALKER"
  print(source)
if source == "3":
  source = "DLSITE"
  print(source)
if source == "4":
  source = "KOBO"
  print(source)
if source == "5":
  source = "PUBU"
  print(source)
else:
  print(source)
translator = input("输入汉化组名称(1.無邪気; 2.文書坊; 3.未來數位出版有限公司; 4.台北原動力視覺有限公司; 5.紳士出版):")
if translator == "1":
  translator = "無邪気漢化組"
  print(translator)
if translator == "2":
  translator = "篆儀通文書坊漢化"
  print(translator)
if translator == "3":
  translator = "未來數位出版有限公司"
  print(translator)
if translator == "4":
  translator = "台北原動力視覺有限公司"
  print(translator)
if translator == "5":
  translator = "紳士出版"
  print(translator)
else:
  print(translator)


############################### 生成manifest列表###############################
zipped = zip(filename_list, extension_list)
g = list(zipped)
m_list = []
c = '''<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'''
m_list.append(c)
for index, a in enumerate(g):
    if a[0] == "blank":
        c = '''<item id="x_blank" href="Text/blank.xhtml" media-type="application/xhtml+xml" properties="svg"/>'''
        m_list.append(c)
    else:
        c = '''<item id="x_{0}" href="Text/{1}.xhtml" media-type="application/xhtml+xml" properties="svg"/>'''.format(str(index+1).zfill(3), a[0])
        m_list.append(c)

for index, a in enumerate(g):
    if a[1] == ".jpg":
        type = "jpeg"
    if a[1] == ".png":
        type = "png"
    if index == 0:
        c = '''<item id="i_{0}" href="Images/{1}{2}" media-type="image/{3}" properties="cover-image"/>'''.format(str(index+1).zfill(3), a[0], a[1], type)
        m_list.append(c)
    else:
        if a[0] == "blank":
            c = '''<item id="i_blank" href="Images/{1}{2}" media-type="image/{3}"/>'''.format(str(index+1).zfill(3), a[0], a[1], type)
            m_list.append(c)
        else:
            c = '''<item id="i_{0}" href="Images/{1}{2}" media-type="image/{3}"/>'''.format(str(index+1).zfill(3), a[0], a[1], type)
            m_list.append(c)
############################### 生成opf文件###############################
u = uuid.uuid4()
date = time.strftime("%Y-%m-%d"+"T"+"%H:%M:%S"+"Z")
f=open("./templates/manga_templates.opf",mode="r",encoding="utf-8")
content = f.read()
keyword1 = "</manifest>"
for x in m_list:
    position1 = content.find(keyword1)
    content = content[:position1] + "\r    " + x + content[position1:]
keyword3 = "id=\"uuid\""
keyword4 = "dcterms:modified"
keyword5 = "id=\"isbn\""
keyword6 = "<dc:publisher>"
keyword7 = "<dc:date>"
keyword8 = "<dc:creator>"
keyword9 = "<dc:title>"
keyword10 = "<dc:language>"
keyword11 = "<dc:source>"
keyword12 = "id=\"cre\""
position3 = content.find(keyword3)
content = content[:position3 + 10] + str(u) + content[position3 + 10:]
position4 = content.find(keyword4)
content = content[:position4 + 18] + str(date) + content[position4 + 18:]
position5 = content.find(keyword5)
content = content[:position5 + 10] + isbn + content[position5 + 10:]
position6 = content.find(keyword6)
content = content[:position6 + 14] + publisher + content[position6 + 14:]
position7 = content.find(keyword7)
content = content[:position7 + 9] + publish_date + content[position7 + 9:]
position8 = content.find(keyword8)
content = content[:position8 + 12] + author + content[position8 + 12:]
position9 = content.find(keyword9)
content = content[:position9 + 10] + title + content[position9 + 10:]
position10 = content.find(keyword10)
content = content[:position10 + 13] + language + content[position10 + 13:]
position11 = content.find(keyword11)
content = content[:position11 + 11] + source + content[position11 + 11:]
position12 = content.find(keyword12)
content = content[:position12 + 9] + translator + content[position12 + 9:]
file = open("./temp/OEBPS/manga.opf",mode="w",encoding="utf-8")
file.write(content)
file.close()
print("已生成manga.opf")
print("生成档案名:","["+isbn+"]","["+author+"]",title,"["+source+"]")

if filename_list[-1] == "blank":
    filename_list.pop()
spine_list = []
for index, name in enumerate(filename_list):
  spine_list.append("x_"+str(index+1).zfill(3)+"|"+name)
file1 = open("./spine_list.txt",mode="w",encoding="utf-8")
for i in spine_list:
    file1.write(i+"\n")
file1.close()