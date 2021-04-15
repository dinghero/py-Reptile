
import time
from PIL import Image
def getpx():
    # //读取验证码图片，转化为灰度图
    img = Image.open('img_tu.png').convert('L')
    # 获取图片尺寸
    size = img.size
    # 获取图片像素值
    im = img.load()
    i = 10
    # 声明列表接收图片处理结果
    int_list = []
    while i < size[1] - 10:
        j = 10
        while j < size[0] - 10:
            value = im[j, i]
            if value < 100:
                if im[j - 1, i] > 200:
                    int_list.append((j - 1))
            j += 1
        i += 1
    # 拷贝列表，去重
    list2 = int_list.copy()
    list2 = list(set(list2))
    # 统计结果集，获取验证码位置 list2[id]
    count = 0
    id = 0
    i = 0
    while i < len(list2):
        temp = int_list.count(list2[i])
        if temp > count:
            id = i
            count = temp
        i += 1
    print('%s出现次数最多：%s次' % (list2[id], count))
    return list2[id]



