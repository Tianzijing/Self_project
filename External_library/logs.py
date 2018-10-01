import os
import time


def get_log_path(file_path, name_path):
    '''
            此方法用于得到日志文件的路径
    '''
    # print(file_path) #Z:\VM\Scripts\workspace_py\SuperClass05\demo\decorator_demo.py
    # print(name_path) #demo.decorator_demo
    # 先处理模块名，用反斜杠替换掉.
    tmp_path = name_path.replace(".", "\\")
    # 根据替换后操作找到在文件路径中所在的位置，以此得到项目的路径
    pos = file_path.find(tmp_path)
    # 截取得到项目路径
    project_path = file_path[:pos]
    # 通过分割得到包名的列表
    name_list = str.split(name_path, ".")
    # 生成日志文件的名字
    log_name = name_list.pop() + "_" + time.strftime("%Y%m%d%H%M%S") + ".log"
    # 定义临时变量，用于存放日志相对目录路径
    tmp = "logs\\"
    # 循环进行日志目录的拼接
    for name in name_list:
        tmp = tmp + name + "\\"
    # 得到日志目录的全路径
    log_dir = project_path + tmp
    # 如果日志目录不存在则新建
    if not os.path.exists(log_dir):
        # print("not exists")
        os.makedirs(log_dir)
    # 得到日志文件的全路径
    log_path = log_dir + log_name
    # print("全路径：", log_dir)
    # print("名称：", log_name)
    # print("日志地址：", log_path)
    # 返回日志路径
    return log_path


def print_log(file_path, comment, mode='a+', encoding="utf-8"):
    # 第一句输出到consle：
    print(comment)
    # 第二句输出到txt："{} 方法第{}次开始执行~~~".format(func.__name__, i+1)
    with open(file=file_path, mode=mode, encoding=encoding) as f:
        print("P\t", comment, file=f)


def log(file_path, msg, mode='a+', encoding="utf-8"):
    '''
            此方法提供日志写入的功能
    '''
    print(msg)
    # 打开日志文件
    fp = open(file=file_path, mode=mode, encoding=encoding)
    # 进行写入操作
    fp.write(msg)
    # 换行
    fp.write("\n")
    # 写完关闭
    fp.close()
