
import requests
import time
import re
from res.ppmh.util_AES import aesDecrypt
from res.sql.linkMysql import insertsqls

nameArray = []
urlArray = []

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }

def load_url(url):
    reponse = requests.get(url, headers=headers)
    time.sleep(1)
    html = reponse.content.decode("utf-8", errors="ignore")
    return html

def paquindex_i(url, key, ajax):
    html = load_url(url)
    name_pattern = r'[te]" id="detxt' + ajax + '">.{10,100}</span>'
    url_pattern = r'listde.php\?act=list&aid=[0-9]{2,3}'
    name_list = re.findall(name_pattern, html)
    url_list = re.findall(url_pattern, html)
    i = 0
    while i < len(url_list):
        url_list[i] = url_list[i]
        name_list[i] = name_list[i][16:].replace('</span>', '')
        name_list[i] = aesDecrypt(key, name_list[i])
        nameArray.append(name_list[i])
        urlArray.append(url_list[i])
        i += 1


def paquindex(url, key):
    html = load_url(url)
    name_pattern = r'[te]" id="detxt">.{10,100}</span>'
    url_pattern = r'listde.php\?act=list&aid=[0-9]{2,3}'
    name_list = re.findall(name_pattern, html)
    url_list = re.findall(url_pattern, html)
    i = 0
    while i < len(url_list):
        url_list[i] = url_list[i].replace('"', '')
        name_list[i] = name_list[i][14:].replace('</span>', '')
        name_list[i] = aesDecrypt(key, name_list[i])
        nameArray.append(name_list[i])
        urlArray.append(url_list[i])
        i += 1

if __name__ == '__main__':
    key = 'YhG78Plkl56Htrqw'
    base_url = 'https://xppmh96.com/'
    # 访问首页
    # paquindex(base_url, key)
    # 访问首页，向下加载
    i = 10
    while i < 16:
        paquindex_i(base_url+'indexp.html?p='+str(i), key, str(i))
        i += 1
    t = 0
    sql = 'INSERT INTO cartoon_title (cartoon_name,cartoon_url,project_id) VALUES\n'

    while t < len(nameArray):
        sql = sql + ' (\''+nameArray[t]+'\',\''+urlArray[t]+'\',1),'
        t += 1
    sql = sql.strip(',')
    print(sql)
    insertsqls(sql)
