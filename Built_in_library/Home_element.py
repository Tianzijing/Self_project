from random import randint

from selenium.webdriver.common.by import By


class Home_element():
    '''
        首页元素
    '''
    # 首行
    LOG_IN_BUTTON = [By.XPATH, "//font[@id='ECS_MEMBERZONE']/a[1]/img"]
    LOG_IN_QUIT = [By.LINK_TEXT, "退出"]
    PURCHASE_LABEL = [By.LINK_TEXT, "购买"]
    POSITIONING_GOODS = [By.CLASS_NAME, "goodsItem"]

    # 标题栏


    def quit(self, driver):
        # 点击退出登录
        driver.find_element(self.LOG_IN_QUIT).click()

    def title(self, driver, title):
        # 点击a标签 图书\音像\电子书
        driver.find_element_by_link_text(title).click()

    def buy(self, driver, value=None, name=None):
        '''
            根据商品位置选择
        '''
        if name == None:
            # 点击a标签 购买 （列表 随机选）
            list_value = driver.find_elements(self.PURCHASE_LABEL)
            # 根据位置选择
            if value:
                value_int = int(value)-1
                list_value[value_int].click()
            else:
                n = len(list_value)
                choose = randint(0, (n-1))
                list_value[choose].click()
        else:
            '''
                根据商品名称选择
                //*[@id="brandList"]/div[1]/h4/span
            '''
            # 定位商品 class="goodsItem" 存为列表
            list_name = driver.find_elements(self.POSITIONING_GOODS)
            for i in list_name:
                text = i.text
                if name in text:
                    i.find_element(self.PURCHASE_LABEL).click()
                    break
                if text[:-3] in name:
                    i.find_element(self.PURCHASE_LABEL).click()
                    break

    def click_image(self, driver, value=None, name=None):
        '''
            根据商品位置选择
        '''
        if name == None:
            # 点击class 图片 （列表 随机选）
            list_value = driver.find_elements(self.POSITIONING_GOODS)
            # 根据位置选择
            if value:
                value_int = int(value) - 1
                list_value[value_int].click()
            else:
                n = len(list_value)
                choose = randint(0, (n - 1))
                list_value[choose].click()
        else:
            '''
                根据商品名称选择
                //*[@id="brandList"]/div[1]/h4/span
            '''
            # 定位商品 class="goodsItem" 存为列表
            list_name = driver.find_elements(self.POSITIONING_GOODS)
            for i in list_name:
                text = i.text
                # print("text = ",text)
                # print("text[:7] = ", text[:7])
                # print("name = ",name)
                if name in text:
                    i.find_element_by_partial_link_text(name).click()
                    break
                if text[:7] in name:
                    i.find_element_by_partial_link_text(text[:7]).click()
                    break

    def search(self, driver, find):
        # 搜索 id keyword
        driver.find_element_by_id("keyword").send_keys(find)
        driver.find_element_by_name("imageField").click()