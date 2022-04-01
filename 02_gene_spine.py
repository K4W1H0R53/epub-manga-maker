import os

s_list = []
with open("./spine_list.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()
    for index, a in enumerate(contents_table):
        if index == 0:
            c = '''<itemref idref="{0}" properties="rendition:page-spread-center"/>'''.format(a)
            s_list.append(c)
        else:
            if index % 2 == 0:
                c = '''<itemref idref="{0}" properties="page-spread-left"/>'''.format(a)
                s_list.append(c)
            else:
                c = '''<itemref idref="{0}" properties="page-spread-right"/>'''.format(a)
                s_list.append(c)

for b in s_list:
    print(b)
# f=open("./temp/OEBPS/manga.opf",mode="r",encoding="utf-8")
# content = f.read()
# keyword2 = "</spine>"
# for i in spine_list:
#     position2 = content.find(keyword2)
#     content = content[:position2] + "\r    " + i + content[position2:]