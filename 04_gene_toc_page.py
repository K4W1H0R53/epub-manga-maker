with open("./contents.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()
    bodymatter_index = 0
    for i in contents_table:
        chapter_name = i.split('|',2)[0]
        page_name = i.split('|',2)[1]
        if i.find("*") != -1:
            bodymatter_index += 1
            print("找到正文章节,章节名为<",chapter_name+"> ,开始页为",page_name)
            continue
        if i.find("#") != -1:
            print("跳过章节,章节名为",chapter_name)