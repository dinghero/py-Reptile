import re
import requests
import time
import random
import os
import pandas as pd
import logging
from logging import handlers

def downloadpicture(values):
    theurl = values.get('url')
    # 文件存储路径
    path = values.get('path')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': 'Hm_lvt_492109f03bd65de28452325006c4a53c=1584163883; security_session_verify=c100ad8a9f56ae6ced36a7a6105a1f3b; Hm_lpvt_492109f03bd65de28452325006c4a53c=1584164468'
    }
    sum = 0
    zu = 0
    i = values.get('starpages')
    while i < values.get('pages'):
        url = theurl + str(i) + '.html'
        reponse = requests.get(url, headers=headers)
        time.sleep(1)
        content = reponse.content.decode("utf-8", errors="ignore")
        # print('第%d:页开始下载' % i)
        # 获取界面上所有组图片
        re_str = re.compile('http://m.win4000.com/meinv.{6,7}html')
        re_name = re.compile('alt=.[\u4e00-\u9fa5a-zA-Z0-9_/./》/《 ]{8,30}')
        re_title = re.compile('tit_icon1">[\u4e00-\u9fa5].*</h2>')
        # 图片类型名称
        filename = re.findall(re_title, content)[0][11:][:-5]
        url_list = re.findall(re_str, content)
        name_list = re.findall(re_name, content)

        # 遍历所有组图片
        list_i = 0
        for the in url_list:
            print('第：%d 页 %d 组开始下载' % (i, (list_i + 1)))
            logger.info('第：%d 页 %d 组开始下载' % (i, (list_i + 1)))
            the = the.split('.html')[0]
            # 进入访问组图片信息
            print('图片组名称' + name_list[list_i])
            logger.info('图片组名称' + name_list[list_i])
            number = 1
            while number < 20:
                picture_list_url = the[:32] + "_" + str(number) + '.html'
                resp = requests.get(picture_list_url, headers=headers)
                time.sleep(6)
                # 判断是否存在此页面
                if resp.status_code == 200:
                    ht = resp.content.decode("utf-8", errors="ignore")
                    # 获取图片资源
                    re_src = re.compile('http://pic1.win4000.com/pic/.{13,20}jpg')
                    picture_src = re.findall(re_src, ht)
                    if len(picture_src) > 0:
                        print('开始尝试下载第：' + str(number) + '张图片，资源路径:' + picture_src[0])
                        logger.info('开始尝试下载第：' + str(number) + '张图片，资源路径:' + picture_src[0])
                        # 访问图片资源
                        picture = requests.get(picture_src[0], headers=headers)
                        while picture.status_code != 200:
                            print('图片资源:' + picture_src[0] + '::访问失败，5秒后重试。。。')
                            logger.info('图片资源:' + picture_src[0] + '::访问失败，5秒后重试。。。')
                            time.sleep(5)
                            picture = requests.get(picture_src[0], headers=headers)
                        time.sleep(1)
                        # 下载图片
                        name = str(name_list[list_i])
                        name = name[5:]
                        filepath = path + filename + "/" + name
                        if os.path.exists(filepath):
                            f = open(filepath + "/img_%d.jpg" % number, "wb")
                            f.write(picture.content)
                            f.close()
                            number += 1
                        else:
                            os.makedirs(filepath)
                            f = open(filepath + "/img_%d.jpg" % number, "wb")
                            f.write(picture.content)
                            f.close()
                            number += 1
                    else:
                        time.sleep(3)
                        number += 1
                else:
                    print('此组照片%d张' % (number - 1))
                    logger.info('此组照片%d张' % (number - 1))
                    break
            list_i = list_i + 1
            print('第：%i 页 %d 组，合计：%d 组下载完成' % (i, list_i, (zu + list_i)))
            logger.info('第：%i 页 %d 组，合计：%d 组下载完成' % (i, list_i, (zu + list_i)))
        time.sleep(random.randint(15, 30))
        zu = zu + 24
        i = i + 1


if __name__ == '__main__':
    args = pd.read_json("package.json", encoding='utf-8')
    values = args.values[0][0]
    print("读取配置文件成功。。。")
    logpath = values.get('log')

    # 加载日志模块
    logger = logging.getLogger('HERO')
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(name)s-%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')
    time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename=logpath, when='D')
    time_rotating_file_handler.setLevel(logging.DEBUG)
    time_rotating_file_handler.setFormatter(formatter)
    logger.addHandler(time_rotating_file_handler)

# 爬取开始
    downloadpicture(values)
