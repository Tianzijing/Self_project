from time import sleep
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Built_in_library import Settings


class User_center_element():

    st = Settings()

    # 元素识别
    COUNTRY = [By.NAME, "country"]
    PROVINCE = [By.NAME, "province"]
    CITY = [By.NAME, "city"]
    DISTRICT = [By.NAME, "district"]
    INPUTBG = [By.CLASS_NAME, "inputBg"]
    ADDRESS_ADD_BUTTON = [By.CLASS_NAME, "bnt_blue_2"]

    def add_shipping_address(self, driver, address=st.address_01):
        # 输入中国 name="country"
        select_country = driver.find_element(self.COUNTRY)
        country = Select(select_country)
        country.select_by_visible_text(address['country'])
        # 输入省份 name="province"
        select_province = driver.find_element(self.PROVINCE)
        province = Select(select_province)
        province.select_by_visible_text(address['province'])
        # 输入市 name="city"
        select_city = driver.find_element(self.CITY)
        city = Select(select_city)
        city.select_by_visible_text(address['city'])
        # 输入区 name="district"
        select_district = driver.find_element(self.DISTRICT)
        district = Select(select_district)
        district.select_by_visible_text(address['district'])
        # class = inputBg 列表 输入 0（姓名）/2（地址）/4（电话）
        inputBg_list = driver.find_elements(self.INPUTBG)
        inputBg_list[0].send_keys(address['name'])
        inputBg_list[2].send_keys(address['address'])
        inputBg_list[4].send_keys(address['phone'])
        # 点击 配送至这个地址 class="bnt_blue_2"
        driver.find_element(self.ADDRESS_ADD_BUTTON).click()

    def user_center(self, driver, module=None):
        # 点击 用户中心
        driver.find_element_by_link_text("用户中心").click()
        # 点击模块
        if module:
            module_str = module
            driver.find_element_by_link_text(module_str).click()
            print("已进入{}模块！".format(module))
        else:
            print("已进入用户中心!")

    def order_operation(self, driver, order_number):
        # 订单列表 div class boxCenterList /table/tbody/tr（索引从 1 个开始）
        # /html/body/div[7]/div[2]/div/div/div/table/tbody/tr[2]
        sleep(2)
        centerlist = driver.find_elements_by_xpath("/html/body/div[7]/div[2]/div/div/div/table/tbody/tr")
        # centerlist = center.find_elements_by_tag_name("tr")
        # print(center)
        print(centerlist)
        for i in centerlist:
            text = i.text
            print(text)
            if order_number in text:
                # /td[5]/font/a
                order_status = i.find_element_by_xpath("//td[5]/font/a")
                order_status_text = order_status.text
                if order_status_text == "确认收货":
                    order_status.click()
                    # 取得弹窗的文本值进行判断
                    alert_text = driver.switch_to_alert().text
                    TestCase.assertEqual(TestCase(), "你确认已经收到货物了吗？", alert_text)
                    # 点击确认
                    driver.switch_to_alert().accept()
                    break
                else:
                    print("前台订单:{} 未完成确认发货断言失败".format(order_number))
            else:
                print("未找到订单：{}".format(order_number))
            try:
                # 已确认收货 span style="color:red" 已完成 /td[5]/font/span
                operat_text = i.find_element_by_xpath("//span[@style='color:red']").text
                TestCase.assertEqual(TestCase(), "已完成", operat_text, "前台确认收货断言失败！")
            except:
                pass

    def check_balances(self, driver):
        # /html/body/div[7]/div[2]/div/div/div/div[5]/a[1]
        self.user_center(driver, module=None)
        balance = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/div/div[5]/a[1]").text
        balance = float(balance[1:-1])
        return balance