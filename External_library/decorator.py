# 此模块提供日志记录和异常重试机制的方法
import traceback
import datetime
from Built_in_library import Settings
from External_library.logs import log


def log_decorator(log_path):
    def inner_decorator(func):
        def do_func(*arg):
            n = Settings().n
            i = 0
            now = datetime.datetime.now()
            log(log_path, "A\t开始时间：{}\t{}".format(
                now.strftime('%Y-%m-%d %H:%M:%S'), func.__name__))
            while True:
                log(log_path, "C\t{}{} 方法第{}次开始执行~~~".format(
                    "  ☆  ", func.__name__, i+1))
                try:
                    func(*arg)
                    break
                except AssertionError as e:
                    log(log_path, "E\t{}{} 执行过程中出现了断言异常，具体信息为：\n\t{}".format(
                        "  ☆  ", func.__name__, str(e)))
                    i += 1
                except:
                    log(log_path, "F\t{}{} 执行过程中出现了其他异常，具体信息为：\n\t{}".format(
                        "  ☆  ", func.__name__, traceback.format_exc()))
                    i += 1
                if i == n:
                    break
                # lg.log("出现非断言异常，即将进行一次重试！速度将会根据配置文件放慢执行！！！！")
            log(log_path, "D\t{}{} 方法执行结束~~~".format("  ☆  ", func.__name__))
            now = datetime.datetime.now()
            log(log_path, "B\t结束时间：{}\t{}\n".format(
                now.strftime('%Y-%m-%d %H:%M:%S'), func.__name__))
        return do_func
    return inner_decorator
