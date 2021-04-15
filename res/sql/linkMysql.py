import pymysql
'''
#                 连接名称，默认127.0.0.1  用户名     # 密码         # 端口，默认为3306 # 数据库名称   # 字符编码
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', port=3306, db='py_reptile', charset='utf8')
# 生成游标对象
cur = conn.cursor()
# SQL语句
sql ="select * from `project_manage`"
# 执行SQL语句
cur.execute(sql)
# 通过fetchall方法获得数据
data = cur.fetchall()
# 打印输出前2条数据
for i in data[:2]:
    print(i)
# 关闭游标
cur.close()
# 关闭连接
conn.close()
'''
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='admin', port=3306, db='py_reptile', charset='utf8')

def insertsql(sql):
    cur = conn.cursor()
    try:
        conn.ping(reconnect=True)
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    conn.close()

def insertsqls(sql):
    cur = conn.cursor()
    conn.ping(reconnect=True)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def selectsql(sql):
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
