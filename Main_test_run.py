# 用于批量执行测试用例 并导出报告
import unittest
import os
import sys
import time
from External_library.HTMLTestRunner import HTMLTestRunner
from Main_test import Test_smoke_test_forward_order


# =================测试集=================
# 实例化一个测试集（测试套件）
suite = unittest.TestSuite()
# 加载一些测试用例
suite.addTest(Test_smoke_test_forward_order("test_smoke_test_forward_order"))


# =================导出报告=================
# 获取当前路径
cur_dir = os.getcwd()
sys.path.append(cur_dir)
now = time.strftime("%Y-%m-%d_%H_%M_%S")
report_folder = cur_dir + os.sep + 'Report' + os.sep
filename = report_folder + now + '_result.html'  # 测试报告的路径名
print(filename)
fp = open(filename, 'wb')  # 以二进制的格式，以写的方式，打开报告文件
runner = HTMLTestRunner(
                        stream=fp,
                        title='ECSHOP_自动化测试报告',
                        description='用例执行情况：')
# runner = unittest.TextTestRunner()
runner.run(suite)
