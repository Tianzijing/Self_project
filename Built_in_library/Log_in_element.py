from time import sleep
from selenium.webdriver.common.by import By

from Built_in_library import Settings
from Built_in_library.Home_element import Home_element


class Log_in_element():

    he = Home_element()
    st = Settings()

    '''
        登录界面元素
    '''
    LOG_IN_USERNAME = [By.NAME, "username"]
    LOG_IN_USERPASSWD = [By.NAME, "password"]
    LOG_IN_IMTY_BUTTON = [By.NAME, "submit"]

    def log_in(self, driver, user):
        '''
            前段登录
        '''
        # 实例化首页元素
        he = self.he
        # 打开前段
        driver.open(self.st.base_url)
        # 点击登录 //*[@id='ECS_MEMBERZONE']/a[1]/img
        try:
            driver.find_element(he.LOG_IN_BUTTON).click()
        except:
            he.quit(driver)
            sleep(1)
            driver.find_element(he.LOG_IN_BUTTON).click()
            print("|---------------------------------------|")
            print("|    这是一个登录安全漏洞！大BUG！！！！！    |")
            print("|---------------------------------------|")
        # 输入用户名 name="username"
        driver.find_element(self.LOG_IN_USERNAME).send_keys(user['name'])
        # 输入密码 name="password"
        driver.find_element(self.LOG_IN_USERPASSWD).send_keys(user['password'])
        # 点击立即登录 name="submit"
        driver.find_element(self.LOG_IN_IMTY_BUTTON).click()

