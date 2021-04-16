

import re

from res.ppmh.p_picture import paqu
from res.ppmh.request_html import load_url

from res.sql.linkMysql import selectsql

imglist = ['LmpwZw==', '5qcGc=']
picture_ids = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5',
               'xMC', 'xMS', 'xMi', 'xMy', 'xNC', 'xNS', 'xNi', 'xNy', 'xOC', 'xOS',
               'yMC', 'yMS', 'yMi', 'yMy', 'yNC', 'yNS', 'yNi', 'yNy', 'yOC', 'yOS',
               'zMC', 'zMS', 'zMi', 'zMy', 'zNC', 'zNS', 'zNi', 'zNy', 'zOC', 'zOS',
               '0MC', '0MS', '0Mi', '0My', '0NC', '0NS', '0Ni', '0Ny', '0OC', '0OS',
               '1MC', '1MS', '1Mi', '1My', '1NC', '1NS', '1Ni', '1Ny', '1OC', '1OS',
               '2MC', '2MS', '2Mi', '2My', '2NC', '2NS', '2Ni', '2Ny', '2OC', '2OS',
               '3MC', '3MS', '3Mi', '3My', '3NC', '3NS', '3Ni', '3Ny', '3OC', '3OS'
               ]

baseurl ='https://0715ch.com/'
picUrl = 'https://0715ch.com/'


def carwing_content(start, cartoon_id):
    sql = 'SELECT c.chapter_id, chapter_name, chapter_url, ct.cartoon_name from chapter c LEFT JOIN cartoon_title ct on ct.cartoon_id = c.cartoon_id where c.chapter_sort >= '\
          +str(start)+' and c.cartoon_id = '+cartoon_id+' ORDER BY chapter_sort'
    list = selectsql(sql)
    for item in list:
        cartoon_name = item[3]
        chapter_id = item[0]
        chapter_name = item[1].replace('?', '')
        url = baseurl + item[2]
        html = load_url(url)
        title_pattern = r'L2ZpbGV.{20}'
        link = re.search(title_pattern, html).group()
        tag = True
        i = 0
        while i < len(picture_ids):
            if i > 8:
                param = 'deimgtxtimg.js?txtimg=' + link + picture_ids[i] + imglist[1] + '&lid=' + str(i)
            else:
                param = 'deimgtxtimg.js?txtimg=' + link + picture_ids[i] + imglist[0] + '&lid=' + str(i)
            insertSql = 'insert into content (content_url,content_sort,chapter_id) value (\'' + param + '\', ' + str(
                i + 1) + ', ' + str(chapter_id) + ')'
            tag = paqu(picUrl + param, 'E:/漫画/' + cartoon_name + "/" + chapter_name, str(i), tag, insertSql)
            # insertsql(insertSql)
            if not tag:
                print('------------------第%d集完成：共%d页--------------' % (start, i))
                break
            i += 1
            print('第%d集：第%d页完成' % (start, i))
        start += 1



if __name__ == '__main__':
    #漫画id
    cartoonId = str(30)
    # 从第 start 章节开始
    chapterStart = 1
    carwing_content(chapterStart, cartoonId)