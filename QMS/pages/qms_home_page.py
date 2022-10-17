from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage

class QmsMainPage(BasePage):

    LOGIN_BUTTON = (By.CLASS_NAME, "customer-login")


    def nav_to_login_page(self):
        self.wait_for(self.LOGIN_BUTTON).click()
        return LoginPage(self.driver)