import requests,re
tags_dict = {
    'male':'男性',
    'female':'女性',
    'other':'其他',
    'mix':'混合',
    'group':'乱交',
    'bondage':'束缚',
    'ffm threesome':'女男女',
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
    'cat girl':'猫娘',
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
    'handjob':'打手枪'
    }


def get_tags_list(gallery_url):
    temp = re.split('\/',gallery_url)
    gid = temp[4]
    gtoken = temp[5]
    tags_list = []
    tags_list_cn = []
    response_content = requests.post(url='https://api.e-hentai.org/api.php', json={"method": "gdata","gidlist": [[gid,gtoken]],"namespace": 1})
    response_content = response_content.text
    print(response_content)
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

def gene_subject():
    tags_list = []
    tags_list_cn = []
    f = open('./tags.txt','r',encoding='utf-8')
    tags_table= f.read().splitlines()
    for i in tags_table:
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

for i in gene_subject()[0]:
    print('<dc:subject>'+i+'</dc:subject>')