import requests,re

tags_dict = {
    'male':'男性',
    'female':'女性',
    'drunk':'饮酒',
    'shotacon':'正太',
    'condom':'避孕套',
    'sleeping':'睡眠',
    'tall man':'高个子',
    'virginity':'童贞',
    'big breasts':'巨乳',
    'blowjob':'口交',
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
    'sweating':'出汗'
    }

def get_gallery_id():
    gurl = input("请输入画廊地址:")
    temp = re.split('\/',gurl)
    gid = temp[4]
    gtoken = temp[5]
    return(gid,gtoken)

def get_tags_list(gid,gtoken):
    tags_list = []
    tags_list_cn = []
    response_content = requests.post(url='https://api.e-hentai.org/api.php', json = {"method": "gdata","gidlist": [[gid,gtoken]],"namespace": 1})
    response_content = response_content.text
    response_content = str(re.findall('\"tags\"\:\[(.*?)\]',response_content))
    tags = response_content.replace('\"','').replace('\'', '').replace('[', '').replace(']', '')
    tags = tags.split(',')
    for i in tags:
        tags_prefix = i.split(':')[0]
        tags_suffix = i.split(':')[1]
        if tags_prefix == "artist" or tags_prefix == "other":
            tag_name = str(tags_prefix) + ":" + str(tags_suffix)
            tags_list.append(tag_name)
            continue
        else:
            tags_prefix_cn = tags_dict.get(tags_prefix)
            tags_suffix_cn = tags_dict.get(tags_suffix)
            tag_name = str(tags_prefix) + ":" + str(tags_suffix)
            tag_name_cn = str(tags_prefix_cn) + ":" + str(tags_suffix_cn)
            tags_list.append(tag_name)
            tags_list_cn.append(tag_name_cn)
    return(tags_list_cn,tags_list)

gallery_id = get_gallery_id()
gid = gallery_id[0]
gtoken = gallery_id[1]
tags_name_en = get_tags_list(gid,gtoken)[0]
tags_name_cn = get_tags_list(gid,gtoken)[1]

for i in tags_name_en:
    print(i,end=',')