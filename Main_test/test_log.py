#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-29 15:57:13
# @Author  : Tian Zijing (504690037@qq.com)
# @Link    : Copyright belongs to the author

import unittest
from Built_in_library import Settings
from External_library.selenium_driver import SeleniumDriver
from External_library.decorator import log_decorator


class Test_Log(unittest.TestCase):

    def setUp(self):
        self.st = Settings()
        self.driver = SeleniumDriver(type=None)
        self.driver.Wait()
        self.base_url = "http://baidu.com"

    @log_decorator(Settings().log)
    def test_log(self):
        # 调用函数
        st = self.st
        # 打开网页
        driver = self.driver
        driver.open(self.base_url)

    def tearDown(self):
        self.driver.quit()
