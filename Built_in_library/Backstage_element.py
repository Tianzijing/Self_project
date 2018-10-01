from asyncio.test_utils import TestCase
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Built_in_library import Settings


class Backstage():

    st = Settings()

    # 后台界面切换
    FRAME_MAIN = "main-frame"
    FRAME_ABOVE = "header-frame"
    FRAME_MENU = "menu-frame"

    BACKSTAGE_ADMIN_NAME = [By.NAME, "username"]
    BACKSTAGE_ADMIN_PASSWORD = [By.NAME, "password"]
    BACKSTAGE_ADMIN_BUTTON = [By.CLASS_NAME, "button"]
    PENDING_ORDER = [By.LINK_TEXT, "待发货订单:"]
    BACKSTAGE_VIEW_ORDER = [By.LINK_TEXT, "查看"]
    GENERATE_A_SHIPPING_ORDER = [By.NAME, "ship"]
    CONFIRM_GENERATE_INVOICE = [By.NAME, "delivery_confirmed"]
    ORDER_SEARCH = [By.NAME, "order_sn"]
    SELECT_ORDER_STATUS = [By.NAME, 'status']
    BACKSTAGE_SEARCH = [By.XPATH, "//input[@value=' 搜索 ']"]
    BACKSTAGE_GO_SHIP = [By.NAME, "to_delivery"]
    BACKSTAGE_SHIP = [By.NAME, "delivery_confirmed"]
    SUCCESSFUL_OPERATION = [By.XPATH, "/html/body/div[1]/div/table/tbody/tr[1]/td[2]"]
    SHIPPED = [By.XPATH, "//div[@id='listDiv']/table[1]/tbody/tr[3]/td[7]"]
    UNREVIEWED_COMMENT = [By.LINK_TEXT, "未审核评论:"]
    COMMENT_SEARCH = [By.NAME, "keyword"]
    SEE_DETAILS = [By.LINK_TEXT, "查看详情"]
    BY_COMMENT_BUTTON = [By.CSS_SELECTOR, "input.button"]
    ENTER_A_COMMENT = [By.NAME, "content"]
    REPLY_TO_COMMENT_CONFIRMATION = [By.NAME, "submit"]


    def log_in_backstage(self, driver):
        try:
            driver.open(self.st.admin_url)
            # 输入用户名 name="username"
            driver.find_element(self.BACKSTAGE_ADMIN_NAME).send_keys(self.st.Admin['name'])
            # 输入密码 name="password"
            driver.find_element(self.BACKSTAGE_ADMIN_PASSWORD).send_keys(self.st.Admin['password'])
            # 点击进入管理中心 class="button"
            driver.find_element(self.BACKSTAGE_ADMIN_BUTTON).click()
        except:
            print("|---------------------------------------|")
            print("|    这是一个登录安全漏洞！大BUG！！！！！    |")
            print("|---------------------------------------|")

    def generate_a_shipping_order(self, driver, order_number):
        '''
            后台 生成发货订单
        '''
        self.frame_main(driver)
        # 点击 a标签 待发货订单:
        driver.find_element(self.PENDING_ORDER).click()
        # 搜索 name="order_sn" 输入 order_number
        self.order_search(driver, order_number)
        # 点击查看 a 查看
        driver.find_element(self.BACKSTAGE_VIEW_ORDER).click()
        try:
            # 点击 生成发货订单 name="ship"
            driver.find_element(self.GENERATE_A_SHIPPING_ORDER).click()
            # 点击 确认生成发货单 name="delivery_confirmed"
            driver.find_element(self.CONFIRM_GENERATE_INVOICE).click()
            sleep(2)
            # 断言 操作成功
            try:
                text = driver.find_element(self.SUCCESSFUL_OPERATION).text
                TestCase.assertEqual(TestCase(), "操作成功", text, "确认生成发货单 断言失败！")
            except:
                print("确认生成发货单 未找到成功信息~~~~~")
        except:
            print("已完成 确认生成发货单 跳过确认生成发货单")

    def order_search(self, driver, order_number):
        # 搜索 name="order_sn" 输入 order_number
        driver.find_element(self.ORDER_SEARCH).send_keys(order_number)
        # 搜索 订单状态 select name="status"
        select_order_status = driver.find_element(self.SELECT_ORDER_STATUS)
        order_status = Select(select_order_status)
        order_status.select_by_visible_text("请选择...")
        # 点击 搜索 input value=" 搜索 "
        driver.find_element(self.BACKSTAGE_SEARCH).click()
        sleep(1)

    def ship(self, driver, order_number):
        '''
            后台 发货
        '''
        # 尝试搜索
        try:
            # 点击 去发货 name="to_delivery"
            driver.find_element(self.BACKSTAGE_GO_SHIP).click()
            # 点击 查看
            driver.find_element(self.BACKSTAGE_VIEW_ORDER).click()
            # 点击 发货 name="delivery_confirmed"
            driver.find_element(self.BACKSTAGE_SHIP).click()

        except:
            self.frame_main(driver)
            # 点击 a标签 待发货订单:
            driver.find_element(self.PENDING_ORDER).click()
            self.order_search(driver, order_number)
        # 断言 操作成功
        try:
            text = driver.find_element(self.SUCCESSFUL_OPERATION).text
            TestCase.assertEqual(TestCase(), "操作成功", text, "发货操作 断言失败！")
        except:
            print("发货操作 未找到成功信息~~~~~")
        # 再断言 name="order_sn"
        self.order_search(driver, order_number)
        try:
            # //div[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]
            text = driver.find_element(self.SHIPPED)
            TestCase.assertEqual(TestCase(), "已发货", text, "发货单列表 断言失败！")
        except:
            print("发货单列表 未找到成功信息~~~~~")

    def review_comments(self, driver, comment_user, comment_admin=None):
        '''
        :说明:
        :   审核评论，如果没有通过，则评论+通过；
        :   如果通过了，则禁止显示
        :return: 管理员评论 or 订单状态
        :   comment_admin_str
        :   comment_status
        '''
        # 切换子界面
        self.frame_main(driver)
        # 点击 未评审
        driver.find_element(self.UNREVIEWED_COMMENT).click()
        # 按评论搜索
        driver.find_element(self.COMMENT_SEARCH).send_keys(comment_user)
        # 点击确认
        driver.find_element(self.BACKSTAGE_SEARCH).click()
        sleep(1)
        # 点击 查看详情
        driver.find_element(self.SEE_DETAILS).click()
        # 点击 允许显示
        comment_status = driver.find_element(self.BY_COMMENT_BUTTON).get_attribute("value")
        user_name = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td/a/b").text
        product_name = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td/b").text
        driver.find_element(self.BY_COMMENT_BUTTON).click()
        # 切回界面
        self.quit_frame(driver)
        # 切换子界面
        self.frame_main(driver)
        # 输入评论
        if comment_admin:
            comment_admin_str = comment_admin
        else:
            comment_admin_str = str(time())
        driver.find_element(self.ENTER_A_COMMENT).send_keys(comment_admin_str)
        # 点击 确认
        driver.find_element(self.REPLY_TO_COMMENT_CONFIRMATION).click()
        if comment_status == "禁止显示":
            print("已禁止显示 {}的评论：{}".format(user_name, comment_user))
        return product_name, user_name, comment_status, comment_admin_str

    def frame_main(self, driver):
        driver.switch_to_frame(self.FRAME_MAIN)

    def frame_above(self, driver):
        driver.switch_to_frame(self.FRAME_ABOVE)

    def frame_menu(self, driver):
        driver.switch_to_frame(self.FRAME_MENU)

    def quit_frame(self, driver):
        driver.switch_to_default_content()

    def return_purchase(self, driver, order_number, comment=None):
        self.find_order(driver, order_number)
        # 点击退货 name = order_number
        return_purchase = driver.find_element_by_name("return")
        text = return_purchase.get_attribute("value")
        if text == "退货":
            return_purchase.click()
        else:
            print("订单{}：目前状态为：订单未完成，不能退货".format(order_number))
        self.quit_frame(driver)
        self.frame_main(driver)
        if comment:
            comment_str = str(comment)
        else:
            comment_str = str(time())
        # name="action_note"
        driver.find_element_by_name("action_note").send_keys(comment_str)
        driver.find_element_by_name("submit").click()
        # /html/body/div[1]/div/table/tbody/tr[1]/td[2]
        prompt = driver.find_element(self.SUCCESSFUL_OPERATION).text
        TestCase.assertEqual(TestCase(), "操作成功", prompt, "退货操作断言失败！")

    def find_order(self, driver, order_number):
        self.frame_main(driver)
        # 点击 a标签 待发货订单:
        driver.find_element(self.PENDING_ORDER).click()
        # 搜索 name="order_sn" 输入 order_number
        self.order_search(driver, order_number)
        # 点击查看 a 查看
        driver.find_element(self.BACKSTAGE_VIEW_ORDER).click()