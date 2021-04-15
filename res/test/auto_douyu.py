from selenium import webdriver
import time
import requests



url = 'https://www.douyu.com/'

#打开谷歌浏览器
proxy = '114.99.2.2:9999'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)
chrome_options.add_argument('...proxy-server=https://27.152.91.211:9999')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(url)


# 查看本机ip，查看代理是否起作用
# browser.get("http://httpbin.org/ip")
# print(browser.page_source)
# browser.quit()

#打开网址
# chrome.get(url)
# time.sleep(2)