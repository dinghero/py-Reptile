import json

import requests

"""
手机端有数据的，尽量模拟手机端来实现，会比电脑端简单很多。
"""

word = input("请输入要翻译的汉字")

#data = {"from": "zh", "to": "en", "query": word, "transtype": "realtime", "simple_means_flag": "3", "sign": "777849.998728", "token": "92c8fa95b0e27c6a890fd376bb41df22"}

data = {
    "smartresult":"dict",
    "smartresult":"rule",
    "i": word,
"from": "AUTO", "to": "AUTO",
    "client":"fanyideskweb",
"doctype": "json",
"action": "FY_BY_REALTlME",
"keyfrom": "fanyi.web"
}
"""

headers = {
"authority": "fanyi.baidu.com",
"method": "POST",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36",
    "x-requested-with": "XMLHttpRequest"

}
"""
headers = {
    "User_agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36"
}

response = requests.post("http://fanyi.youdao.com/translate", data=data, headers = headers)

ret_str = response.content.decode("utf-8")
ret = json.loads(ret_str)

print("%s  翻译后的结果为：" % word)
print(ret["translateResult"][0][0]["tgt"])
