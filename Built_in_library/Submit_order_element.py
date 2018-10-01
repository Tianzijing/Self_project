import random
from random import randint
from selenium.webdriver.common.by import By
from Built_in_library import Settings, User_center_element


class Submit_order_element():

    '''
        提交订单页面
    '''

    uc = User_center_element()
    st = Settings()

    SUBMIT_ORDER_BUTTON = [By.XPATH, "//input[@type='image']"]
    DELIVERY_METHOD_LIST = [By.XPATH, "//table[@id='shippingTable']/tbody/tr"]
    DELIVERY_METHOD = [By.NAME, "shipping"]
    PAY_METHOD_LIST = [By.XPATH, "//table[@id='paymentTable']/tbody/tr"]
    PAY_METHOD = [By.NAME, "payment"]
    ORDER_NUMBER = [By.XPATH, "//font[@style='color:red']"]

    def submit_order_button(self, driver, method=None, pay=None):

        '''
                尝试去点击配送方式
                如果没有 则填写地址
        '''

        uc = self.uc
        st = self.st
        # 尝试是否需要添加地址
        try:
            # 输入地址
            uc.add_shipping_address(driver)
        except:
            pass
        # 点击配送方式
        self.delivery_method(driver, method)
        # 点击付款方式
        self.pay_method(driver, pay)
        # 尝试找到 提交订单 input type="image"
        driver.find_element(self.SUBMIT_ORDER_BUTTON).click()
        # 导出订单号 font style="color:red"
        order_number = driver.find_element(self.ORDER_NUMBER).text
        print("订单号：{}".format(order_number))
        return order_number

    def delivery_method(self, driver, method='城际快递'):
        # id="shippingTable"    /tbody/tr
        method_list = driver.find_elements(self.DELIVERY_METHOD_LIST)
        method_number = 0
        if method == '城际快递':
            method_number = 1
        elif method == '申通快递':
            method_number = 2
        elif method == '邮局平邮':
            method_number = 3
        elif method == '随机' or method == None:
            method_number = 0
        else:
            print("请输入正确配送方式：城际快递、申通快递、邮局平邮")
        # 选择
        if method_number != 0:
            method_list[method_number].find_element(*self.DELIVERY_METHOD).click()
        else:
            n = randint(1, 3)
            method_list[n].find_element(*self.DELIVERY_METHOD).click()

    def pay_method(self, driver, pay='余额支付'):
        # paymentTable
        # id="shippingTable"    /tbody/tr
        method_list = driver.find_elements(self.PAY_METHOD_LIST)
        method_number = 0
        if pay == '余额支付':
            method_number = 1
        elif pay == '货到付款':
            method_number = 3
        elif pay == '随机' or pay == None:
            method_number = 0
        else:
            print("请输入正确配送方式：余额支付、货到付款")
        # 选择
        if method_number != 0:
            method_list[method_number].find_element(*self.PAY_METHOD).click()
        else:
            a = [1, 3]
            n = random.sample(a, 1)
            n = n[0]
            method_list[n].find_element(*self.PAY_METHOD).click()