from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShopCheckoutPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def get_page(self):
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')

    def checkout(self, fname, lname, zip_code):
        self._driver.find_element(By.ID, "first-name").send_keys(fname)
        self._driver.find_element(By.ID, "last-name").send_keys(lname)
        self._driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def click_to_continue(self):
        self._driver.find_element(By.ID, "continue").click()