from time import time, sleep
from unittest import TestCase


class Product_details():


    def product_reviews(self, driver, comment=None):
        # //form[@id="commentForm"]/table/tbody/tr[1]/td[2]
        user_name = driver.find_element_by_xpath("//form[@id='commentForm']/table/tbody/tr[1]/td[2]").text
        if user_name == "匿名用户":
            email = str(time()*1000)[:13] + "@123.com"
            driver.find_element_by_name("email").send_keys(email)
        if comment:
            comment_user = str(comment)
        else:
            comment_user = str(time())
        driver.find_element_by_name("content").send_keys(comment_user)
        # //div[@id="commentForm"]/table/tbody/tr[5]/td/input
        # driver.find_element_by_xpath("//div[@id='commentForm']/table/tbody/tr[5]/td/input").click()
        driver.find_element_by_css_selector("input.f_r").click()
        sleep(3)
        # 取得弹窗的文本值进行判断
        alert_text = driver.switch_to_alert().text
        TestCase.assertEqual(TestCase(), "您的评论已成功发表, 请等待管理员的审核!", alert_text)
        # 点击确认
        driver.switch_to_alert().accept()
        return user_name, comment_user