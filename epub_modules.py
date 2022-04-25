import os,uuid,time
import numpy as np
import cv2

def uuid_id():
    text = str(uuid.uuid4())
    return text

class Generate_field:
    def __init__(self,field_name,character=None):
        self.field_name = field_name
        self.character = character
    def common(self):
        field = '''<dc:{0}>{1}</dc:{0}>'''.format(self.character,self.field_name)
        print(field)
        return(field)
    def identifier(self):
        if "-" in self.field_name:
            id_type = "other"
        else:
            id_type = "isbn"
        field = '''<dc:identifier id=\"{0}\">{1}</dc:identifier>'''.format(id_type,self.field_name)
        print(field)
        return(field)
    def creator(self):
        field = '<dc:creator id=\"cre0\">'+self.field_name+'</dc:creator>'
        print(field)
        return(field)
    def translator(self):
        field = '''<dc:creator id=\"cre1\">{0}</dc:creator>\n<meta refines="#cre1" property="role" scheme="marc:relators">trl</meta>'''.format(self.field_name)
        print(field)
        return(field)

class Metadate:
    def __init__(self,identifier,publisher,date,author,title,language,source,contributor,tags,description=["test","description"],translator=None):
        self.identifier = identifier
        self.publisher = publisher[0]
        self.publisher_char = publisher[1]
        self.date = date[0]
        self.date_char = date[1]
        self.author = author
        self.title = title[0]
        self.title_char = title[1]
        self.description = description[0]
        self.description_char = description[1]
        self.language = language[0]
        self.language_char = language[1]
        self.source = source[0]
        self.source_char = source[1]
        self.contributor = contributor[0]
        self.contributor_char = contributor[1]
        self.translator = translator
        self.tags = tags[0]
        self.tags_char = tags[1]

    def gene_metadate_list(self):
        metadate_list = []
        a = Generate_field(field_name = self.identifier)
        metadate_list.append(a.identifier())
        a = Generate_field(self.publisher, self.publisher_char)
        metadate_list.append(a.common())
        a = Generate_field(self.date, self.date_char)
        metadate_list.append(a.common())
        a = Generate_field(self.author)
        metadate_list.append(a.creator())
        a = Generate_field(self.title, self.title_char)
        metadate_list.append(a.common())
        a = Generate_field(self.description,self.description_char)
        metadate_list.append(a.common())
        a = Generate_field(self.language,self.language_char)
        metadate_list.append(a.common())
        a = Generate_field(self.source,self.source_char)
        metadate_list.append(a.common())
        a = Generate_field(self.contributor,self.contributor_char)
        metadate_list.append(a.common())
        if not self.translator:
            return (metadate_list)
        else:
            a = Generate_field(self.translator)
            metadate_list.append(a.translator())
        s = self.tags
        for i in s:
            a = Generate_field(i,self.tags_char)
            metadate_list.append(a.common())
        return (metadate_list)


path_image = os.walk("./temp/OEBPS/Images")

def gene_xhtml(title):
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
            page_html = xhtml_content.format(src_width, src_height, file_name,title[0])
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

def gene_opf(metadate_list,manifest_list,spine_list):
    with open('./templates/manga_templates.opf','r',encoding='utf-8') as f:
        content = f.read()
        x = str(uuid.uuid4())
        post_uuid = content.find('</dc:identifier>')
        content = content[:post_uuid] + "\r    " + x + content[post_uuid:]
        y = time.strftime("%Y-%m-%d"+"T"+"%H:%M:%S"+"Z",time.localtime())
        post_metadate = content.find('<meta property="dcterms:modified">')
        content = content[:post_metadate] + "\r    " + y + content[post_metadate:]

        for a in metadate_list:
            post_metadate = content.find('<meta property="rendition:spread">auto</meta>')
            content = content[:post_metadate] + "\r    " + a + content[post_metadate:]
        for b in manifest_list:
            post_manifest = content.find('</manifest>')
            content = content[:post_manifest] + "\r    " + b + content[post_manifest:]
        for c in spine_list:
            post_spine = content.find('</spine>')
            content = content[:post_spine] + "\r    " + c + content[post_spine:]
    file = open("./temp/OEBPS/manga.opf",mode="w",encoding="utf-8")
    file.write(content)
    file.close()