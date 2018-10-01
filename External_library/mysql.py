import time
from datetime import datetime
import pymysql

# 修改实名验证信息
def ch_certification(user, number=2):
    if type(user) == dict:
        # 定义MySQL语句
        sql = "UPDATE ds_userinfo SET certification = " + str(number) + " WHERE name = '" + user['name'][1] + "';"
    elif type(user) == str:
        sql = "UPDATE ds_userinfo SET certification = " + str(number) + " WHERE name = '" + user + "';"
    else:
        print('请输入正确姓名格式')
    # 调用查询方法
    verifyCode_1 = get_certification(user)
    # 调用修改方法
    ch_execute_sql(sql)
    # 调用查询方法
    verifyCode = get_certification(user)
    # 返回验证码
    print("验证已修改为：%s → %s" %(verifyCode_1, verifyCode))

# 查询实名验证信息
def get_certification(user):
    if type(user) == dict:
        # 定义MySQL语句
        sql = "SELECT certification FROM ds_userinfo WHERE name = '" + user['name'][1] + "' ORDER BY id desc LIMIT 0, 1;"
    elif type(user) == str:
        sql = "SELECT certification FROM ds_userinfo WHERE name = '" + user + "' ORDER BY id desc LIMIT 0, 1;"
    else:
        print('请输入正确姓名格式')
    # 调用查询方法
    certification = execute_sql(sql)[0][0]
    # 返回验证状态
    return certification

# 查询用户信息
def get_users(user=None):
    if user != None:
        # 定义MySQL语句
        sql = "SELECT * FROM ds_user WHERE username = '" + user['name'][1] + "' ORDER BY id desc;"
    else:
        # 定义MySQL语句
        sql = "SELECT * FROM ds_user ORDER BY id desc;"
    # 调用查询方法
    users_message = execute_sql(sql)
    # 返回验证状态
    return users_message

# 充值记录查询
def get_recharge(number):
    # 定义MySQL语句
    sql = "SELECT * FROM ds_recharge WHERE number = '" + str(number) + "';"
    # 调用查询方法
    recharge_list = execute_sql(sql)
    # 返回验证状态
    return recharge_list

def get_verifyCode(session):
    # 定义MySQL语句
    sql = "SELECT code FROM ds_verifyCode WHERE session = '" + session + "' ORDER BY id desc LIMIT 0, 1;"
    # 调用查询方法
    verifyCode = execute_sql(sql)[0][0]
    # 返回验证码
    return verifyCode

# ============链接数据库==========
def execute_sql(sql):
    # 连接数据库
    db = pymysql.connect("172.31.17.67", "root", "123456", "p2p")
    # 使用cursor()方法创建一个游标对象cursoe
    cursor = db.cursor()
    # 使用execute()方法执行SQL查询
    cursor.execute(sql)
    # 使用fetchall()获取所有数据
    data = cursor.fetchall()
    # 关系数据连接
    db.close()
    # 返回数据内容
    return data

def ch_execute_sql(sql, url="172.31.17.67"):
    # 连接数据库
    db = pymysql.connect(url, "root", "123456", "p2p")
    # 使用cursor()方法创建一个游标对象cursoe
    cursor = db.cursor()
    # 使用execute()方法执行SQL查询
    cursor.execute(sql)
    # 提交
    db.commit()
    # 关系数据连接
    db.close()
