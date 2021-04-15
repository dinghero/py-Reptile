
import sys
import logging.config
from logging import handlers

####利用sys输出日志到文件中
# log_file = open("message.log", "a")
# sys.stdout = log_file
# i=1
# print ("Now all print info will be wr")
# print('第：%d 页 %d 组开始下载' % (i, (i+1)))
# log_file.close()

'''
%(name)s：Logger的名字
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
'''
####调用logging模块打印日志
# logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG)

####打印日志到test.log文件中
# logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG,
#                     filename='test.log',
#                     filemode='a'
#                     )


####读取配置文件打印日志到控制台
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
# logging.info('info级别，一般用来打印一些正常的操作信息')
# logging.warning('waring级别，一般用来打印警告信息')
# logging.error('error级别，一般用来打印一些错误信息')
# logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')


###输出日志到控制台和日志文件中
logger = logging.getLogger('HERO')
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(name)s-%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# file_handler = logging.FileHandler('test.log')
# file_handler.setLevel(level=logging.INFO)
# file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# stream_handler.setFormatter(formatter)

# 若改为 when='S'，则以秒为周期进行切割，没有后缀的为最新日志文件。
time_rotating_file_handler = handlers.TimedRotatingFileHandler(filename='rotating_test.log', when='D')
time_rotating_file_handler.setLevel(logging.DEBUG)
time_rotating_file_handler.setFormatter(formatter)


# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
logger.addHandler(time_rotating_file_handler)

logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
logger.info('info级别，一般用来打印一些正常的操作信息')
logger.warning('waring级别，一般用来打印警告信息')
logger.error('error级别，一般用来打印一些错误信息')
logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

