import os
path_image = os.walk("./books/test")

filename_list = []
extension_list = []
for path, dir_list, file_list in path_image:
    for index, file_name in enumerate(sorted(file_list)):
        filename = os.path.splitext(file_name)[0]
        extension = os.path.splitext(file_name)[1]
        filename_list.append(filename)
        extension_list.append(extension)

with open("./test1.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()
    for a in contents_table:
        if index == 0:
            c = '''<itemref idref="x_{0}" properties="rendition:page-spread-center"/>'''.format(str(index+1).zfill(3))
            s_list.append(c)
        else:
            if index % 2 == 0:
                c = '''<itemref idref="x_{0}" properties="page-spread-left"/>'''.format(str(index+1).zfill(3))
                s_list.append(c)
            else:
                c = '''<itemref idref="x_{0}" properties="page-spread-right"/>'''.format(str(index+1).zfill(3))
                s_list.append(c)


with open("./test2.txt",'w',encoding='UTF-8-sig') as t:
    for a in s_list:
        t.write(a+"\n")
        
# f=open("./temp/OEBPS/manga.opf",mode="r",encoding="utf-8")
# content = f.read()
# keyword2 = "</spine>"
# for i in spine:
#     position2 = content.find(keyword2)
#     content = content[:position2] + "\r    " + i + content[position2:]