from asyncio import wait_for
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.qms_logged_in_page import QmsLoggedInPage

class LoginPage(BasePage):

    EMAIL_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    SUBMIT_BUTTON = (By.CLASS_NAME, "wSubmitBtn")
    PASSWORD_ERROR = (By.ID, 'Password-error')
    EMAIL_ERROR = (By.ID, 'Email-error')



    def be_logged_in(self, email, password):

        self.wait_for(self.EMAIL_FIELD).send_keys(email)
        self.wait_for(self.PASSWORD_FIELD).send_keys(password)
        self.wait_for(self.SUBMIT_BUTTON).click()
        return QmsLoggedInPage(self.driver)

    def read_email_error(self):
        return self.wait_for(self.EMAIL_ERROR).text

    def read_password_error(self):
        return self.wait_for(self.PASSWORD_ERROR).text

