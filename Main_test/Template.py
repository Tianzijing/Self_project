import unittest
from Built_in_library import Settings, Shopping_cart_element
from Built_in_library import Backstage, User_center_element
from Built_in_library import Home_element, Log_in_element
from Built_in_library import Submit_order_element
from External_library.decorator import log_decorator
from External_library.selenium_driver import SeleniumDriver


class Test_NAME(unittest.TestCase):

    def setUp(self):
        self.he = Home_element()
        self.le = Log_in_element()
        self.st = Settings()
        self.sc = Shopping_cart_element()
        self.so = Submit_order_element()
        self.bs = Backstage()
        self.uc = User_center_element()
        self.driver = SeleniumDriver(type=None)
        self.driver.Wait()
        self.base_url = self.st.base_url

    @log_decorator(Settings().log)
    def test_NAME(self):
        # 调用函数
        he = self.he
        le = self.le
        st = self.st
        sc = self.sc
        so = self.so
        bs = self.bs
        uc = self.uc
        # 打开网页
        driver = self.driver
        driver.open(self.base_url)
        # 执行测试内容
        pass

    def tearDown(self):
        self.driver.quit()
