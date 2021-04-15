import numpy as np
import pandas as pd
import requests
import urllib

# https://www.xicidaili.com/nn
#'http://www.66ip.cn/'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
proxy = '222.95.144.24:3000'
proxies = {
    'http': 'http://' + proxy
}
# pr = '112.250.107.3:53281'
url = 'http://www.66ip.cn/'
# url = 'https://www.xicidaili.com/nn'
# 代理处理器
proxy_handler = urllib.request.ProxyHandler(proxies)
# 创建自己的opener
opener = urllib.request.build_opener(proxy_handler)
# 拿着代理ip去发送请求
html = opener.open(url).read()

# html = requests.get(url, headers=headers, proxies=pr)
print(html)
data = pd.read_html(html.text)
result = data[0]
# result.reindex(columns=columns)
# print(result)
ser_list =result[['存活时间']].values
ser_list = list(ser_list)
llist = []
for s in ser_list:
    if '天' in s[0]:
        llist.append(True)
    else:
        llist.append(False)
element = result[['类型', 'IP地址', '端口', '存活时间', '服务器地址']]
res = element[llist]
print(res)
