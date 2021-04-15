from selenium import webdriver
import time
import requests



url = 'https://egame.qq.com/'

#打开谷歌浏览器
chrome = webdriver.Chrome()


#打开网址
chrome.get(url)
time.sleep(2)

#点击登录
login = chrome.find_element_by_class_name('navbar-icon-login')
login.click()
time.sleep(2)
#跳转至登录iframe模块上pip
chrome.switch_to.frame('_egame_login_frame_qq_') # _egame_login_frame_qq_
chrome.switch_to.frame('ptlogin_iframe')
time.sleep(1)

mima = chrome.find_element_by_id('switcher_plogin')
mima.click()
name = chrome.find_element_by_id('u')
name.send_keys('195795386')

password = chrome.find_element_by_id('p')
password.send_keys('1654315.')
sub = chrome.find_element_by_class_name('btn')
sub.click()
time.sleep(2)
#跳转至验证码iframe
chrome.switch_to.frame('tcaptcha_iframe')

tu = chrome.find_element_by_id('slideBg')
url = tu.get_attribute('src')


resp = requests.get(url)
f = open("../image/img_tu.png", "wb")
f.write(resp.content)
f.close()


# but = chrome.find_element_by_id('tcaptcha_drag_thumb') #tcaptcha_drag_thumb   tcaptcha_drag_button
but = chrome.find_element_by_class_name('unselectable')

# but.click()
time.sleep(3)

act = webdriver.ActionChains(chrome)



act.drag_and_drop_by_offset(but, 17, 0).perform()
# act.click_and_hold(but).move_by_offset(10, 0).perform()
# act.release(but)

#登录账号


