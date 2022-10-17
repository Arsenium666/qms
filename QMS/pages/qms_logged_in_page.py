from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QmsLoggedInPage(BasePage):
    CUSTOMER_MAIL = (By.CLASS_NAME, 'customer-mail')

    def read_email(self):
        return self.find(self.CUSTOMER_MAIL).text
