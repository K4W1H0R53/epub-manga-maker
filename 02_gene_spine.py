def gene_spine(*page):
    if page is None:
        print("无新增空白页面")
    else:
        x = 0
        for i in page:
            filename_list.insert(i - 1 + x, "blank")
            x += 1
        if filename_list[-1] == "blank":
            filename_list.pop()
    s_list = []
    for index, name in enumerate(filename_list):
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
    return (s_list)

spine = gene_spine()
f=open("./temp/OEBPS/manga.opf",mode="r",encoding="utf-8")
content = f.read()
keyword2 = "</spine>"
for i in spine:
    position2 = content.find(keyword2)
    content = content[:position2] + "\r    " + i + content[position2:]