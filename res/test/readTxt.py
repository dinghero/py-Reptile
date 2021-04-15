'''
阅读TXT电子书拆分章节

'''
import os

filepath = 'D:/17336.txt'
txt = ''
try:
    file = open(filepath, 'r', encoding='utf-8')
    txt = file.read()
    # print(txt)
# except(Exception):
#     print(Exception)
finally:
    file.close()
txt = txt.split('------------')

namelist =[]
for name in txt:
    name = name.split('\n\n')[1]
    namelist.append(name)
print(namelist)