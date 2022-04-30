import uuid,time,csv,requests,re,os
import pandas as pd
import numpy as np
import cv2

tags_dict = {
    'male':'男性',
    'female':'女性',
    'other':'其他',
    'mixed':'混合',
    'group':'乱交',
    'bondage':'束缚',
    'ffm threesome':'女男女',
    'mmf threesome':'男女男',
    'dilf':'大叔',
    'drunk':'饮酒',
    'shotacon':'正太',
    'condom':'避孕套',
    'sleeping':'睡眠',
    'tall man':'高个子',
    'virginity':'童贞',
    'big breasts':'巨乳',
    'blowjob':'口交',
    'bukkake':'颜射',
    'cheating':'出轨',
    'exhibitionism':'露出癖',
    'fingering':'手指抚摸',
    'hairy':'阴毛茂盛',
    'kissing':'接吻',
    'masturbation':'自慰',
    'milf':'熟女',
    'nakadashi':'中出',
    'ponytail':'单马尾',
    'prostitution':'卖春',
    'stockings':'长筒袜',
    'sweating':'出汗',
    'freckles':'雀斑',
    'business suit':'西装',
    'defloration':'破处',
    'fishnets':'渔网',
    'hair buns':'丸子头',
    'impregnation':'受孕',
    'kimono':'和服',
    'lingerie':'情趣内衣',
    'nurse':'护士',
    'pantyhose':'连裤袜',
    'twintails':'双马尾',
    'glasses':'眼镜',
    'sex toys':'性玩具',
    'garter belt':'吊带袜',
    'swimsuit':'泳装',
    'paizuri':'乳交',
    'bikini':'比基尼',
    'footjob':'足交',
    'sumata':'素股',
    'kemonomimi':'兽耳',
    'fox girl':'狐娘',
    'catgirl':'猫娘',
    'schoolgirl uniform':'女生制服',
    'schoolboy uniform':'男生制服',
    'double penetration':'双重插入',
    'cheerleader':'啦啦队员',
    'cunnilingus':'舔阴',
    'deepthroat':'深喉',
    'tickling':'挠痒',
    'urethra insertion':'尿道插入',
    'netorare':'寝取',
    'anal':'肛交',
    'femdom':'女性主导',
    'yandere':'病娇',
    'yuri':'百合',
    'handjob':'打手枪',
    'sister':'姐妹',
    'small breasts':'贫乳',
    'incest':'乱伦',
    'gokkun':'饮精',
    'cum swap':'交换精液',
    'bbm':'胖男人',
    'collar':'项圈',
    'leash':'狗链',
    'facial hair':'胡子',
    'sundress':'夏装',
    'tail':'尾巴',
    'wet clothes':'湿身',
    'dark skin':'黑皮',
    'gloves':'手套',
    'school swimsuit':'死库水',
    'ghost':'幽灵',
    'muscle':'肌肉',
    'apron':'围裙',
    'pixie cut':'精灵头',
    'tomboy':'假小子',
    'waitress':'女侍者装',
    'cousin':'表姐妹',
    'niece':'侄女',
    'breast feeding':'哺乳',
    'inverted nipples':'乳头内陷',
    'lolicon':'萝莉',
    'teacher':'教师',
    'beauty mark':'美人痣',
    'tracksuit':'运动服',
    'tanlines':'晒痕',
    'x-ray':'透视',
    'blindfold':'遮眼布',
    'chikan':'痴汉',
    'clothed female nude male':'裸男',
    'layer cake':'夹心蛋糕',
    'phimosis':'包茎',
    'prostate massage':'前列腺按摩',
    'small penis':'小小鸟',
    'ahegao':'啊嘿颜',
    'harem':'后宫',
    'pantyjob':'内裤交',
    'blackmail':'勒索',
    'bride':'婚纱',
    'shimaidon':'姐妹丼',
    'twins':'双胞胎',
    'big ass':'大屁股',
    'fundoshi':'六尺褌',
    'gyaru':'辣妹',
    'voyeurism':'偷窥',
    'urination':'排尿',
    'piercing':'穿孔',
    'pregnant':'怀孕',
    'age progression':'年龄增长',
    'miko':'巫女',
    'sole male':'单男主',
    'aunt':'阿姨',
    'bandages':'绷带',
    'bisexual':'双性恋',
    'daughter':'女儿',
    'hidden sex':'隐蔽性交',
    'mother':'母亲',
    'oyakodon':'母女丼',
    'rape':'强奸',
    'sarashi':'缠胸布',
    'stomach deformation':'腹部变形',
    'inseki':'姻亲',
    'bbw':'丰腴',
    'bike shorts':'自行车短裤',
    'bloomers':'布鲁马',
    'maid':'女仆',
    'tankoubon':'单行本',
    'oni':'鬼娘',
    'thick eyebrows':'浓眉',
    '故事线':'story arc',
    'old man':'老男人',
    'filming':'摄像',
    'hotpants':'热裤',
    'leg lock':'勾腿'
    }

def gene_metadata(identifier,database=None):
    if database:
        url = database
        metadata = pd.read_csv(url,sep=",",index_col='FD_ID',keep_default_na=False)
        metadata = metadata.loc[identifier]
        publisher = metadata[4]
        print('出版社:',publisher)
        publish_date = metadata[8]
        print('出版日期:',publish_date)
        author = metadata[5]
        print('作者:',author)
        title = metadata[3]
        print('标题:',title)
        description = metadata[11]
        description = description.replace('&','&amp;')
        print('描述:',description)
        series = metadata[12]
        print('系列:',series)
        series_id = metadata[13]
        print('系列编号:',series_id)
        publisher_link_cn = metadata[10]
        publisher_link_cn = publisher_link_cn.replace('&','&amp;')
        print('出版社链接(中文):',publisher_link_cn)
        publisher_link_jp = metadata[9]
        print('出版社链接(日文):',publisher_link_jp)
        eh_link = metadata[16]
        print('eh链接:',eh_link)
        contributor = metadata[17]
        print('上传者:',contributor)
        source = metadata[18]
        print('图源:',source)
        return(identifier,publisher,publish_date,author,title,description,series,series_id,publisher_link_cn,publisher_link_jp,eh_link,contributor,source)
    else:
        return 0

def gene_subject(gallery_url):
    temp = re.split('\/',gallery_url)
    print(temp)
    gid = temp[4]
    print('gallery gid is',gid)
    gtoken = temp[5]
    print('gallery gtoken is',gtoken)
    response_content = requests.post(url='https://api.e-hentai.org/api.php', json={"method": "gdata","gidlist": [[gid,gtoken]],"namespace": 1})
    response_content = response_content.text
    print(response_content)
    response_content = str(re.findall('\"tags\"\:\[(.*?)\]',response_content))
    tags = response_content.replace('\"','').replace('\'', '').replace('[', '').replace(']', '')
    tags = tags.split(',')
    f = open('./tags.txt','w',encoding='utf-8')
    tags_list = []
    tags_list_cn = []
    t = open('./metadata.txt','a',encoding='utf-8')
    for i in tags:
        tags_prefix = i.split(':')[0]
        tags_suffix = i.split(':')[1]
        if tags_prefix == 'language' or tags_prefix == 'artist':
            tag_name = str(tags_prefix) + ":" + str(tags_suffix)
            tags_list.append(tag_name)
            f.write(i+',')
            print('去除作者及语言标签')
        else:
            tags_prefix_cn = tags_dict.get(tags_prefix)
            tags_suffix_cn = tags_dict.get(tags_suffix)
            tag_name = str(tags_prefix) + ":" + str(tags_suffix)
            tag_name_cn = '''<dc:subject>{0}</dc:subject>\n'''.format(str(tags_prefix_cn) + ":" + str(tags_suffix_cn))
            t.write(tag_name_cn)
            tags_list.append(tag_name)
            tags_list_cn.append(tag_name_cn)
            f.write(i+',')
    f.close()
    t.close()
    return(tags_list_cn,tags_list)

def gene_xhtml(title):
    path_image = os.walk("./temp/OEBPS/Images")
    filename_list = []
    extension_list = []
    for path, dir_list, file_list in path_image:
        for index, file_name in enumerate(sorted(file_list)):
            filename = os.path.splitext(file_name)[0]
            extension = os.path.splitext(file_name)[1]
            filename_list.append(filename)
            extension_list.append(extension)
            img = cv2.imdecode(np.fromfile(os.path.join(path,file_name), dtype=np.uint8), 1)
            src_width = img.shape[1]
            src_height = img.shape[0]
            xhtml_content = open("./templates/blank_templates.xhtml","r",encoding="utf-8")
            xhtml_content = xhtml_content.read()
            page_html = xhtml_content.format(src_width, src_height, file_name,title)
            f = open("./temp/OEBPS/Text/" + os.path.splitext(file_name)[0] + ".xhtml", mode="w", encoding="utf-8")
            f.write(page_html)
            f.close()
            spine_file = []
            for index, name in enumerate(filename_list):
                spine_file.append("x_"+str(index+1).zfill(3)+"|"+name)
            f = open("./spine_list.txt",mode="w",encoding="utf-8")
            for i in spine_file:
                f.write(i +"\n")
            f.close()

            zipped = zip(filename_list, extension_list)
            g = list(zipped)
            m_list = []
            c = '''<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'''
            m_list.append(c)
            for index, a in enumerate(g):
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
                    c = '''<item id="i_{0}" href="Images/{1}{2}" media-type="image/{3}"/>'''.format(str(index+1).zfill(3), a[0], a[1], type)
                    m_list.append(c)
    return(m_list)

def gene_spine_list():
    s_list = []
    with open("./spine_list.txt",'r',encoding='UTF-8-sig') as f:
        contents_table= f.read().splitlines()
        for index, a in enumerate(contents_table):
            a = a.split('|',1)[0]
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
    return(s_list)

d = input("请选择数据库(1.未来数位; 2.原动力视觉; 3.绅士出版; 4.自定义):")
if d == "1":
    database = 'https://raw.githubusercontent.com/K4W1H0R53/tankoubon/main/tw/future_digi.csv'
if d == "2":
    database = 'https://raw.githubusercontent.com/K4W1H0R53/tankoubon/main/tw/d_art.csv'
if d == "3":
    database = 'https://raw.githubusercontent.com/K4W1H0R53/tankoubon/main/tw/gman.csv'
else:
    pass

m_list = []
uuid_field = '''<dc:identifier id="uuid">{0}</dc:identifier>\n'''.format(str(uuid.uuid4()))
m_list.append(uuid_field)

identifier = input('请输入出版社编号:')
meta = gene_metadata(identifier,database)

if meta[10]:
    url = meta[10]
    subject = gene_subject(url)[0]
    eh_link_field = 'eh:'+meta[10]
    identifier_field = '''    <dc:identifier>{0}</dc:identifier>\n'''.format(meta[0].lower()+':'+meta[8]+', '+meta[1]+':'+meta[9]+', '+eh_link_field)
    m_list.append(identifier_field)

else:
    print('无eh链接')
    identifier_field = '''    <dc:identifier>{0}</dc:identifier>\n'''.format(meta[0].lower()+':'+meta[8]+', '+meta[1]+':'+meta[9])
    m_list.append(identifier_field)

publisher_field = '''<dc:publisher>{0}</dc:publisher>\n'''.format(meta[1])
m_list.append(publisher_field)

publish_date_field = '''<dc:date>{0}</dc:date>\n'''.format(meta[2])
m_list.append(publish_date_field)

author_field = '''<dc:creator id="cre0">{0}</dc:creator>\n'''.format(meta[3])
m_list.append(author_field)

title_field = '''<dc:title>{0}</dc:title>\n'''.format(meta[4])
m_list.append(title_field)

description_field = '''<dc:description>\n{0}\n    </dc:description>\n'''.format(meta[5])
m_list.append(description_field)

language_field = '''<dc:language>{0}</dc:language>\n'''.format('zh-TW')
m_list.append(language_field)

source_field = '''<dc:source>{0}</dc:source>\n'''.format(meta[12])
m_list.append(source_field)

contributor_field = '''<dc:contributor>{0}</dc:contributor>\n'''.format(meta[11])
m_list.append(contributor_field)

if not (meta[6] is None):
    print('本书不属于任何系列')
    pass
else:
    series_field = '''<meta name="calibre:series" content={0}/>\n'''.format(meta[6])
    m_list.append(series_field)
    series_id_field = '''<meta name="calibre:series_index" content={0}/>\n'''.format(meta[7])
    m_list.append(series_id_field)

t = input("输入图源类型(1.扫图; 2.Bookwalker; 3.DLsite; 4.KOBO; 5.PUBU):")
if t == "1":
    source =  "SCAN"
if t == "2":
    source = "BOOKWALKER"
if t == "3":
    source = "DLSITE"
if t == "4":
    source = "KOBO"
if t == "5":
    source = "PUBU"
source_field = '''<dc:source>{0}</dc:source>\n'''.format(source)
m_list.append(source_field)

if d == "1":
    translator = "未來數位出版有限公司"
if d == "2":
    translator = "台北原動力視覺有限公司"
if d == "3":
    translator = "紳士出版"
translator_field1 = '''<dc:creator id="cre1">{0}</dc:creator>\n'''.format(translator)
m_list.append(translator_field1)
translator_field2 = '<meta refines="#cre1" property="role" scheme="marc:relators">trl</meta>\n'
m_list.append(translator_field2)

modified_date_field = '''<meta property="dcterms:modified">{0}</meta>\n'''.format(time.strftime("%Y-%m-%d"+"T"+"%H:%M:%S"+"Z",time.localtime()))
m_list.append(modified_date_field)

if meta[10]:
    url = meta[10]
    subject = gene_subject(url)[0]
    for i in subject:
        m_list.append(i)
else:
    print('无eh链接')

f = open('./metadata.txt','w',encoding='utf-8')
for i in m_list:
    f.write(i)
f.close()

f = open('./templates/manga_templates.opf','r',encoding='utf-8')
content = f.read()
for x in m_list:
    post = content.find('    <meta property="rendition:spread">auto</meta>')
    content = content[:post] + "    " + x + content[post:]

m_list = gene_xhtml(meta[4])
s_list = gene_spine_list()
for b in m_list:
    post_manifest = content.find('</manifest>')
    content = content[:post_manifest] + "\r    " + b + content[post_manifest:]
for c in s_list:
    post_spine = content.find('</spine>')
    content = content[:post_spine] + "\r    " + c + content[post_spine:]

file = open("./test.opf",mode="w",encoding="utf-8")
file.write(content)
file.close()

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
command = input("请输入"+contents_dict[0]+"页面文件名:")
contents_element.append(contents_dict[0]+"|"+command+"|\r")
######################## 确认书名页 ########################
command = input("是否存在书名页(y/n): ")
trueorfalse(command)
if command == "y":
    command = input("请输入"+contents_dict[3]+"页面文件名:")
    trueorfalse(command)
    contents_element.append(contents_dict[3]+"|"+command+"|\r")
if command == "n":
    pass
command = input("请输入"+contents_dict[1]+"页面文件名:")
trueorfalse(command)
contents_element.append(contents_dict[1]+"|"+command+"|toc\r")
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
f = f.read().format(meta[4])
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
import zipfile,pathlib
dict = pathlib.Path("./temp")
# with zipfile.ZipFile("./library/["+identifier+"]","["+author+"]",+title,"["+source+"]","["+contributor+"]"".epub","a",zipfile.ZIP_STORED) as archive:
with zipfile.ZipFile("./library/test.epub","w",zipfile.ZIP_STORED) as archive:
    archive.writestr("mimetype", "application/epub+zip")
    for file_path in dict.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(dict))