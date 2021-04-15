
import re
import requests
import time
import random
import os

theurl = "http://m.win4000.com/meitu_33_"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie':'Hm_lvt_492109f03bd65de28452325006c4a53c=1584163883; security_session_verify=c100ad8a9f56ae6ced36a7a6105a1f3b; Hm_lpvt_492109f03bd65de28452325006c4a53c=1584164468'

}

#循环访问页面
#记录总个数
sum =0
zu = 0
i = 1

url = theurl+str(i)+'.html'
reponse = requests.get(url, headers=headers)
time.sleep(5)
content = reponse.content.decode("utf-8", errors="ignore")
print('第%d:页开始下载' % i)
# 获取界面上所有组图片
re_str = re.compile('http://m.win4000.com/meinv.{6,7}html')
re_name= re.compile('alt=.[\u4e00-\u9fa5a-zA-Z0-9_/./》/《]{8,30}')
url_list = re.findall(re_str, content)
name_list = re.findall(re_name, content)
# print(name_list)
#遍历所有组图片
list_i = 0

# 进入访问组图片信息
print('图片组名称' + name_list[list_i])
number = 1
for the in url_list:
    the = the.split('.html')[0]
    picture_list_url = the[:32] + "_" + str(number) + '.html'
while number < 20:
    picture_list_url = the[:32] + "_" + str(number) + '.html'
    resp = requests.get(picture_list_url, headers=headers)
    time.sleep(20)
    # 判断是否存在此页面
    if resp.status_code == 200:
        print('资源访问成功')
    else:
        print('访问失败')
        break