import epub_modules as epub
import os,sys,uuid,time,cv2,pathlib
import numpy as np


a = 0
t = input("请选择源文件类型(1.日版; 2.台版|英版|民间汉化版):")
identifier = input("输入ISBN:")
publisher = input("输入出版社名称(1.wani; 2.got; 3.core; 4.akaneshinsha; 5.hit; 6.bavel; 7.ktc; 8.kuroe; 9.mujin):")
if publisher == "1":
  publisher = ["ワニマガジン社","publisher"]
if publisher == "2":
  publisher = ["GOT","publisher"]
if publisher == "3":
  publisher = ["コアマガジン","publisher"]
if publisher == "4":
  publisher = ["茜新社","publisher"]
if publisher == "5":
  publisher = ["ヒット出版社","publisher"]
if publisher == "6":
  publisher = ["文苑堂","publisher"]
if publisher == "7":
  publisher = ["KILL TIME COMMUNICATION","publisher"]
if publisher == "8":
  publisher = ["クロエ出版","publisher"]
if publisher == "9":
  publisher = ["ティーアイネット","publisher"]
date = [input("输入发售日期:"),"date"]
author = input("输入作者名:")
title = [input("输入作品名:"),"title"]

if t == "1":
    language = ["ja","language"]
else:
    a = input("输入语言(1.中文; 2.繁体中文; 3.英文):")
    if a == "1":
        language = ["zh-CN","language"]
    if a == "2":
        language = ["zh-TW","language"]
    if a == "3":
        language = ["en-US","language"]

if a == "3":
  source = ["FAKKU","source"]
else:
  a = input("输入图源类型(1.扫图; 2.Bookwalker; 3.DLsite; 4.KOBO; 5.PUBU):")
  if a == "1":
    source =  ["SCAN","source"]
  if a == "2":
    source = ["BOOKWALKER","source"]
  if a == "3":
    source = ["DLSITE","source"]
  if a == "4":
    source = ["KOBO","source"]
  if a == "5":
    source = ["PUBU","source"]
  
if t != "1":
  translator = input("输入翻译者名称(1.無邪気; 2.文書坊; 3.未來數位出版有限公司; 4.台北原動力視覺有限公司; 5.紳士出版; 6.FAKKU):")
  if translator == "1":
      translator = "無邪気漢化組"
  if translator == "2":
      translator = "篆儀通文書坊漢化"
  if translator == "3":
      translator = "未來數位出版有限公司"
  if translator == "4":
      translator = "台北原動力視覺有限公司"
  if translator == "5":
      translator = "紳士出版"
  if translator == "6":
      translator = "FAKKU"
else:
  translator = None
uploader = [input("输入上传者:"),"uploader"]

##################################
input("按回车生成元数据")
##################################
b = epub.Metadate(identifier=identifier, publisher=publisher, date=date, author=author, title=title, language=language, source=source, uploader=uploader, translator=translator)
metadate_list= b.gene_metadate_list()

##################################
input("按回车生成opf及xhtml")
##################################
manifest_list = epub.gene_xhtml(title)

##################################
input("按回车生成spine_list")
##################################
spine_list = epub.gene_spine_list()

##########################################################################################################################################
input("将metadate_list、manifest_list、spine_list合并并生成manga.opf")
##########################################################################################################################################
epub.gene_opf(metadate_list, manifest_list, spine_list)

##########################################################################################################################################
input("生成目录列表")
##########################################################################################################################################
def trueorfalse(a):
    if not a:
        print("输入值不符合要求，结束脚本")
        sys.exit()
    else:
        return

contents_element = []
japanese_dict = ["表纸","目次","表纸と目次","標題紙","あとがき","奧付","とらのあな特典","メロンブツクス特典"]
chinese_dict = ["封面","目錄","封面及目錄","書名頁","後記","版權頁","虎之穴特典","蜜瓜特典"]
z = input("请选择字典(1.繁体中文(适用于台版单行本); 2.日文(适用于日文或者民间汉化版))")
trueorfalse(z)
if z == "1":
    contents_dict = chinese_dict[:]
if z == "2":
    contents_dict = japanese_dict[:]
######################## 确认epub封面项 ########################
cover_filename = input("请输入epub封面文件名(此项用于显示epub预览封面): ")
trueorfalse(cover_filename)
contents_element.append(contents_dict[0]+"|"+cover_filename+"|cover\r")
######################## 确认正文封面及目录 ########################
command = input("封面与目录是否在同一页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入"+contents_dict[2]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[2]+"|"+command+"|toc\r")
if command == "n":
    command = input("请输入"+contents_dict[0]+"页面文件名:")
    contents_element.append(contents_dict[0]+"|"+command+"|\r")
    command = input("请输入"+contents_dict[1]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[1]+"|"+command+"|toc\r")
######################## 确认书名页 ########################
command = input("是否存在书名页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入"+contents_dict[3]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[3]+"|"+command+"|\r")
if command == "n":
    pass
######################## 确认彩图页 ########################
command = input("是否存在彩图插画(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入 COLOR ILLUST 页面文件名:")
    trueorfalse(command)
    contents_element.append("COLOR ILLUST|"+command+"|\r")
if command == "n":
    pass
######################## 确认彩图页 ########################
command = input("是否存在黑白插画(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入 GRAYSCALE ILLUST 页面文件名:")
    trueorfalse(command)
    contents_element.append("GRAYSCALE ILLUST|"+command+"|\r")
if command == "n":
    pass
######################## 确认正文目录 ########################
i = 1
location_list = []
while i > 0:
    t = input("正文章节是否结束(y/n):")
    if t == "y":
        print("正文章节录入完毕")
        break
    else:
        if i == 1:
            chapter_name = input("添加章节名称:")
            chapter_page = input(chapter_name+"起始页为:")
            contents_element.append(chapter_name+"|"+chapter_page+"|bodymatter\r")
            location_element = '''<a xlink:href="{0}.xhtml" target="_top"><rect fill-opacity="0.0" x="" y="" width="" height=""><title>{1}</title></rect></a>\r'''.format(chapter_page,chapter_name)
            location_list.append(location_element)
            i+=1
        else:
            chapter_name = input("添加章节名称:")
            chapter_page = input(chapter_name+"起始页为:")
            contents_element.append(chapter_name+"|"+chapter_page+"|\r")
            location_element = '''<a xlink:href="{0}.xhtml" target="_top"><rect fill-opacity="0.0" x="" y="" width="" height=""><title>{1}</title></rect></a>\r'''.format(chapter_page,chapter_name)
            location_list.append(location_element)
            i+=1        
######################## 确认后记 ########################
command = input("是否存在后记页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入"+contents_dict[4]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[4]+"|"+command+"|\r")
if command == "n":
    pass
######################## 确认版权页 ########################
command = input("是否存在版权页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入"+contents_dict[5]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[5]+"|"+command+"|colophon\r")
if command == "n":
    pass
######################## 确认特典页 ########################
command = input("是否存在特典页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("是否存在虎之穴特典(y/n):")
    if command == "y":
        command = input("请输入"+contents_dict[6]+"页面文件名:")
        trueorfalse(command)
        contents_element.append(contents_dict[6]+"|"+command+"|\r")
    else:
        pass
    command = input("是否存在蜜瓜特典(y/n):")
    if command == "y":
        command = input("请输入"+contents_dict[7]+"页面文件名:")
        trueorfalse(command)
        contents_element.append(contents_dict[7]+"|"+command+"|\r")
    else:
        pass
else:
    pass

f = open("./contents.txt",mode="a",encoding="utf-8")
for i in contents_element:
    f.write(i)
print("目录列表生成完毕")
f.close()

f = open("./location.txt",mode="a",encoding="utf-8")
for i in location_list:
    f.write(i)
f.close()

##########################################################################################################################################
input("确认contents.txt并生成nav.xhtml")
##########################################################################################################################################
contents = []   ## 用于储存章节名
pages = []  ## 用于储存章节开始页文件名
landmarks = []   ## 用于储存landmark

with open("./contents.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()
    for i in contents_table:
        contents.append(i.split('|',2)[0])
        pages.append(i.split('|',2)[1])
        landmarks.append(i.split('|',2)[2])

zipped_list = zip(landmarks,pages,contents)
total = list(zipped_list)
toc_list = []
landmarks_list = []
for x in total:
    if not x[0]:
        pass
    else:
        landmarks_element = '''<li><a epub:type="{0}" href="Text/{1}.xhtml">{2}</a></li>'''.format(x[0],x[1],x[2])
        landmarks_list.append(landmarks_element)
    toc_element = '''<li><a href="Text/{0}.xhtml">{1}</a></li>'''.format(x[1],x[2])
    toc_list.append(toc_element)

f=open("./templates/nav_templates.xhtml",mode="r",encoding="utf-8")
f = f.read().format(title)

for a in toc_list:
    post = f.find("</ol>")
    f = f[:post] + a + "\r        "  + f[post:]
for b in landmarks_list:
    post1 = f.find("</ol>")
    post2 = f.find("</ol>", post1+1)
    f = f[:post2] + b + "\r        "  + f[post2:]
file = open("./temp/OEBPS/nav.xhtml",mode="w",encoding="utf-8")
file.write(f)
file.close()
##########################################################################################################################################
input("打包epub")
##########################################################################################################################################
dict = pathlib.Path("./temp")
with zipfile.ZipFile("./["+identifier+"]","["+author+"]",+title,"["+source+"]","["+uploader+"]"".epub","a",zipfile.ZIP_STORED) as archive:
    archive.writestr("mimetype", "application/epub+zip")
    for file_path in dict.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(dict))