
# 增加header
import requests
import base64
import os
import time

from res.pachong.util_AES import aesDecrypt
from res.sql.linkMysql import insertsql


def paqu(url, filepath, name, tag, insertSql ):
    key = 'YhG78Plkl56Htrqw'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    reponse = requests.get(url, headers=headers)
    time.sleep(1)
    txt = reponse.content.decode("utf-8", errors="ignore")
    if 'Warning' in txt:
        tag = False
        return tag
    img = txt[txt.find(' = "') + 4:]
    img = aesDecrypt(key, img)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(filepath+'/'+name + '.png', 'wb') as f:
        f.write(base64.b64decode(img))
        # insertSql = insertSql + '\'' + img + '\')'
        insertsql(insertSql)
    return tag
