import pytest
from selenium import webdriver
from pages.qms_home_page import QmsMainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://testing.earlyone.com")

    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return QmsMainPage(driver)