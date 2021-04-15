
import requests
import re
import time

# https://www.xicidaili.com/nn


def getiplist(_url):

    i = 2
    while i < 5:
        url = _url + '%d'%i + '.html'
        response = requests.get(url)
        response.encoding = 'gb2312'
        html = response.text
        pattern = re.compile('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*.{0,10}[0-9]{4,5}.{0,85}[\u4e00-\u9fa5]{4}')
        maplist = re.findall(pattern, html)
        j = 0
        while j < len(maplist):
            iplist.append(maplist[j])
            j += 1
        i += 1
        time.sleep(2)
def makeip(list):
    j = 0
    while j < len(list):
        pat1 = re.compile('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]')
        pat2 = re.compile('[0-9]{4,5}')
        pat3 = re.compile('[\u4e00-\u9fa5]{2,15}')
        str = list[j]
        station = '  location:'
        _ip = re.findall(pat1, str)[0]
        _dk = re.findall(pat2, str)[0]
        _be = re.findall(pat3, str)[0]
        str = _ip+':'+_dk +station+_be
        proxlit.append(str)
        j += 1

if __name__ == '__main__':
    url = 'http://www.66ip.cn/'
    iplist = []
    proxlit = []
    getiplist(url)
    i =0
    while i < len(iplist):
        print(iplist[i])
        i +=1
    makeip(iplist)
    # txt = ''
    # i = 0
    # while i < len(proxlit):
    #     print(proxlit[i])
    #     txt = txt +proxlit[i]+'\\n'
    #     i +=1
    file = open('../image/ip_poxy.txt', mode='w', encoding='utf8')
    i =0
    while i < len(proxlit):
        file.write(proxlit[i]+'\n')
        i +=1
    file.close()
    print('获取成功')
