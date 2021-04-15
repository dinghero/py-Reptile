
import requests
import time
import re

from res.pachong.util_AES import aesDecrypt
from res.sql.linkMysql import insertsql


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }


def load_url(url):
    reponse = requests.get(url, headers=headers)
    time.sleep(1)
    html = reponse.content.decode("utf-8", errors="ignore")
    return html


def analysis_html(html, url_pattern, title_pattern):
    url_list = re.findall(url_pattern, html)
    title_list = re.findall(title_pattern, html)
    i = 0
    while i < len(url_list):
        url_list[i] = url_list[i]
        title_list[i] = title_list[i][7:].replace('</span>', '')
        title_list[i] = aesDecrypt('YhG78Plkl56Htrqw', title_list[i])
        i += 1
    return url_list, title_list


#爬取首页
def crawling_chapter_one(base_url, cartoon_id):
    url = base_url+'0'
    html = load_url(url)
    url_pattern = r'style.php\?act=style&aid=.{3}&cid=[0-9]{4,6}'
    title_pattern = r'detxt\">.{20,100}</span>'
    url_list, title_list = analysis_html(html, url_pattern, title_pattern)
    sql = 'insert into chapter (chapter_name,chapter_url,chapter_sort,project_id,cartoon_id) values'
    base = 1
    t = 0
    while t < len(url_list):
        sql = sql + ' (\'' + title_list[t] + '\',\'' + url_list[t] + '\',' + str(t + base) + ',1,'+cartoon_id+'),'
        t += 1
    sql = sql.strip(',')
    insertsql(sql)
    return True


#爬取加载页
def crawling_chapter_i(base_url, ajax, cartoon_id):
    url = base_url+ajax
    html = load_url(url)
    if len(html) <65:
        return False
    url_pattern = r'style.php\?act=style&aid=.{3}&cid=[0-9]{4,6}'
    title_pattern = r'etxt' + ajax + '\">.{20,100}</span>'
    url_list, title_list = analysis_html(html, url_pattern, title_pattern)
    sql = 'insert into chapter (chapter_name,chapter_url,chapter_sort,project_id,cartoon_id) values'
    base = int(ajax) + 2
    t = 0
    while t < len(url_list):
        sql = sql + ' (\'' + title_list[t] + '\',\'' + url_list[t] + '\',' + str(t + base) + ',1,'+cartoon_id+'),'
        t += 1
    sql = sql.strip(',')
    insertsql(sql)
    return True


if __name__ == '__main__':
    cartoonId = str(30)
    baseUrl = 'https://0715ch.com/listde.php?act=list&aid=615&desc=0&ajax='
    #爬取首页
    # crawling_chapter_one(baseUrl, cartoonId)
    #爬取加载页
    loadAjax = 59
    while crawling_chapter_i(baseUrl, str(loadAjax), cartoonId):
        loadAjax = loadAjax + 10

