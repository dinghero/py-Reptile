
import requests
import time
import re

from res.pachong.util_AES import aesDecrypt
from res.sql.linkMysql import insertsql
ajax = str(59)
url = 'https://0715ch.com/listde.php?act=list&aid=572&desc=0&ajax='+ajax

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }

reponse = requests.get(url, headers=headers)
time.sleep(1)
html = reponse.content.decode("utf-8", errors="ignore")

url_pattern = r'style.php\?act=style&aid=.{3}&cid=[0-9]{4,6}'
title_pattern = r'detxt'+ajax+'\">.{20,100}</span>'
# title_pattern = r'detxt\">.{20,100}</span>'
url_list = re.findall(url_pattern, html)
title_list = re.findall(title_pattern, html)
i = 0
while i < len(url_list):
    url_list[i] = url_list[i]
    title_list[i] = title_list[i][7:].replace('</span>', '')
    title_list[i] = aesDecrypt('YhG78Plkl56Htrqw', title_list[i])
    i += 1
t = 0
base = int(ajax)+2
# base = 1
sql = 'insert into chapter (chapter_name,chapter_url,chapter_sort) values'
while t < len(url_list):
    sql = sql + ' (\'' + title_list[t] + '\',\'' + url_list[t] + '\',' + str(t+base) + '),'
    t += 1
sql = sql.strip(',')
insertsql(sql)

