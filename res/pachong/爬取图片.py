
import requests
import base64
import os
import time

from res.pachong.util_AES import aesDecrypt

basetxtimg = 'L2ZpbGVzLzgwODMwLzEwM'
# <8 imglist[0] >8 imglist[1]
imglist = ['LmpwZw==', '5qcGc=']

picture = 'Tg3OS8'
path = 'E:/漫画/'
start = 0

picture_ids = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5',
               'xMC', 'xMS', 'xMi', 'xMy', 'xNC', 'xNS', 'xNi', 'xNy', 'xOC', 'xOS',
               'yMC', 'yMS', 'yMi', 'yMy', 'yNC', 'yNS', 'yNi', 'yNy', 'yOC', 'yOS',
               'zMC', 'zMS', 'zMi', 'zMy', 'zNC', 'zNS', 'zNi', 'zNy', 'zOC', 'zOS',
               '0MC', '0MS', '0Mi', '0My', '0NC', '0NS', '0Ni', '0Ny', '0OC', '0OS',
               '1MC', '1MS', '1Mi', '1My', '1NC', '1NS', '1Ni', '1Ny', '1OC', '1OS',
               '2MC', '2MS', '2Mi', '2My', '2NC', '2NS', '2Ni', '2Ny', '2OC', '2OS',
               '3MC', '3MS', '3Mi', '3My', '3NC', '3NS', '3Ni', '3Ny', '3OC', '3OS'
               ]
lii = ['Tg3Ni8','Tg3Ny8','Tg3OC8','Tg3OS8','Tg4MC8','Tg4MS8','Tg4Mi8','Tk5OS8','jExOC8','jIxOS8',
      'jMxMy8','jQxNS8','jQ3MS8','jU3MC8','jY3NC8','jc2Ny8','jk2OS8','zA3My8','zQ0MS8','zU5NC8',
      'xY4OC8','xkwMi8'
      ]

def paqu(url, name, tag):
    key = 'YhG78Plkl56Htrqw'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    reponse = requests.get(url, headers=headers)
    time.sleep(1)
    txt = reponse.content.decode("utf-8", errors="ignore")
    # req = request.Request(url=url, headers=headers)
    # response = request.urlopen(req)
    # txt = response.read().decode('utf-8')
    if 'Warning' in txt:
        tag = False
        return tag
    img = txt[txt.find(' = "') + 4:]
    img = aesDecrypt(key, img)
    filepath = path+'第'+str(start+1)+'集'
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(filepath+'/'+name + '.png', 'wb') as f:
        f.write(base64.b64decode(img))
    return tag

if __name__ == '__main__':
    key = 'YhG78Plkl56Htrqw'
    base_url = 'https://0715ch.com/deimgtxtimg.js?txtimg='
    li = ['Tg3Ni8', 'Tg3Ny8', 'Tg3OC8', 'Tg3OS8', 'Tg4MC8', 'Tg4MS8', 'Tg4Mi8', 'Tk5OS8', 'jExOC8', 'jIxOS8',
           'jMxMy8', 'jQxNS8', 'jQ3MS8', 'jU3MC8', 'jY3NC8', 'jc2Ny8', 'jk2OS8', 'zA3My8', 'zQ0MS8', 'zU5NC8'

           ]
    while start < len(li):
        it = li[start]
        i = 0
        tag = True
        while i < len(picture_ids):
            name = picture_ids[i]
            if i > 8:
                param = basetxtimg + it + name + imglist[1] + '&lid=' + str(i)
            else:
                param = basetxtimg + it + name + imglist[0] + '&lid=' + str(i)
            url = base_url + param
            tag = paqu(url, str(i), tag)
            # time.sleep(0.5)
            if not tag:
                print('第%d集完成：共%d页' % (start+1, i))
                break
            i = i + 1
            print('第%d集：第%d页完成' % (start+1, i))
        start = start + 1
    print('结束')
