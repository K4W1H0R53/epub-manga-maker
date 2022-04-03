import os
import sys

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
######################## 确认自定义页面 ########################
command = input("是否存在自定义章节(y/n): ")
if command == "y":
    command1 = input("请输入自定义章节名:")
    trueorfalse(command1)
    command2 = input("请输入自定义章节页面文件名:")
    trueorfalse(command1)
    contents_element.append(command1+"|"+command2+"|\r")
else:
    pass

######################## 确认正文目录 ########################
i = 1
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
            i+=1
        else:
            chapter_name = input("添加章节名称:")
            chapter_page = input(chapter_name+"起始页为:")
            contents_element.append(chapter_name+"|"+chapter_page+"|\r")
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

f = open("./test.txt",mode="a",encoding="utf-8")
for i in contents_element:
    f.write(i)
print("目录列表生成完毕")