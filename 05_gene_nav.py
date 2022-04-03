import os,sys

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
        