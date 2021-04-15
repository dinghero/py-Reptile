
import time
from PIL import Image

# img = pl.imread("../image/img_tu.png")

#//获取图片大小
# size = img.shape
# print(size)
img = Image.open('img_tu.png').convert('L')
size = img.size


print(size)
# img.show()
im = img.load()
print(size[1])
i=55

while i < 130:
    j = 501
    while j < 580:
        im[j, i] = 0
        # print('水平像素：%s的像素值%s' % (i, value))
        j += 1
    i +=1


img.show()




'''

cv2.imshow("验证码", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
