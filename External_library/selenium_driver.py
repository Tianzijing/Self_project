# 封装Selenium相关方法，以便于提供回放速度的控制功能
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from Built_in_library import Settings
from External_library.Chrome import Chrome_flash
from External_library.logs import log


class SeleniumDriver(object):

    log_path = Settings().log

    def __init__(self, type=None):
        '''
            初始化指定的浏览器驱动
        '''
        # 得到webdriver
        self.driver = Chrome_flash()
        # self.driver = WebDriver(command_executor='http://172.31.23.143:4444/wd/hub',
        #                         desired_capabilities=DesiredCapabilities.CHROME)
        # 实例化基本配置
        st = Settings()
        # 获取放慢速度
        if type is None:
            self.speed = st.speed_default
        else:
            self.speed = st.speed_down
        log(self.log_path, "G\t初始化指定的浏览器驱动~~~")

    # 初始化等待
    def Wait(self):
        driver = self.driver
        # 设置元素识别超时时间
        driver.implicitly_wait(15)
        # 设置页面加载超时时间
        driver.set_page_load_timeout(15)
        # 设置异步脚本加载超时时间
        driver.set_script_timeout(15)
        log(self.log_path, "G\t加载初始化等等~~~")

    def open(self, base_url):
        # 调用webdriver真正相应的方法
        self.driver.get(base_url)
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t打开网页：{}~~~".format(base_url))

    def quit(self):
        # 调用webdriver真正相应的方法
        self.driver.quit()
        log(self.log_path, "G\t退出当前网页网页~~~")

    def find_element_by_id(self, ID):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 ID = {}".format(ID))
        # 返回找到的元素对象
        return self.driver.find_element_by_id(ID)

    def find_element_by_name(self, name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 NAME = {}".format(name))
        # 返回找到的元素对象
        return self.driver.find_element_by_name(name)

    def find_element_by_class_name(self, class_name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 CLASS_NAME = {}".format(class_name))
        # 返回找到的元素对象
        return self.driver.find_element_by_class_name(class_name)

    def find_element_by_tag_name(self, tag_name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 TAG_NAME = {}".format(tag_name))
        # 返回找到的元素对象
        return self.driver.find_element_by_tag_name(tag_name)

    def find_element_by_link_text(self, link_text):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 LINK_NAME = {}".format(link_text))
        # 返回找到的元素对象
        return self.driver.find_element_by_link_text(link_text)

    def find_element_by_partial_link_text(self, partial_link_text):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 PARTIAL_LINK_NAME = {}".format(partial_link_text))
        # 返回找到的元素对象
        return self.driver.find_element_by_partial_link_text(partial_link_text)

    def find_element_by_xpath(self, xpath):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 XPATH = {}".format(xpath))
        # 返回找到的元素对象
        return self.driver.find_element_by_xpath(xpath)

    def find_element_by_css_selector(self, css_selector):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 CSS_SELECTOR = {}".format(css_selector))
        # 返回找到的元素对象
        return self.driver.find_element_by_css_selector(css_selector)

    def find_element(self, By):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在定位 {} = {}".format(*By))
        # 返回找到的元素对象
        return self.driver.find_element(*By)

    '''
        列表
    '''

    def find_elements_by_id(self, ID):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 ID = {}".format(ID))
        # 返回找到的元素对象
        return self.driver.find_elements_by_id(ID)

    def find_elements_by_name(self, name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 NAME = {}".format(name))
        # 返回找到的元素对象
        return self.driver.find_elements_by_name(name)

    def find_elements_by_class_name(self, class_name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 CLASS_NAME = {}".format(class_name))
        # 返回找到的元素对象
        return self.driver.find_elements_by_class_name(class_name)

    def find_elements_by_tag_name(self, tag_name):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 TAG_NAME = {}".format(tag_name))
        # 返回找到的元素对象
        return self.driver.find_elements_by_tag_name(tag_name)

    def find_elements_by_link_text(self, link_text):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 LINK_NAME = {}".format(link_text))
        # 返回找到的元素对象
        return self.driver.find_elements_by_link_text(link_text)

    def find_elements_by_partial_link_text(self, partial_link_text):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 PARTIAL_LINK_NAME = {}".format(partial_link_text))
        # 返回找到的元素对象
        return self.driver.find_elements_by_partial_link_text(partial_link_text)

    def find_elements_by_xpath(self, xpath):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 XPATH = {}".format(xpath))
        # 返回找到的元素对象
        return self.driver.find_elements_by_xpath(xpath)

    def find_elements_by_css_selector(self, css_selector):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 CSS_SELECTOR = {}".format(css_selector))
        # 返回找到的元素对象
        return self.driver.find_elements_by_css_selector(css_selector)

    def find_elements(self, By):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t正在列表定位 {} = {}".format(*By))
        # 返回找到的元素对象
        return self.driver.find_elements(*By)

    def switch_to_frame(self, frame):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t切换内置窗口至 {}".format(frame))
        # 返回找到的元素对象
        return self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t切会主窗口")
        # 返回找到的元素对象
        return self.driver.switch_to.default_content()

    def switch_to_alert(self):
        # 调用webdriver真正相应的方法
        # 加个等待时间
        sleep(self.speed)
        log(self.log_path, "G\t弹出窗口点击 确认")
        # 返回找到的元素对象
        return self.driver.switch_to_alert()
