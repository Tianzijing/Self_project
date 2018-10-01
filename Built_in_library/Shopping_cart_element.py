from selenium.webdriver.common.by import By


class Shopping_cart_element():

    SHOPPING_BUTTON = [By.XPATH, "//img[@alt='checkout']"]

    def shopping_button(self, driver):
        driver.find_element(self.SHOPPING_BUTTON).click()