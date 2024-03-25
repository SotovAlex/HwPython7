from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShopCartPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def get_page(self):
        self._driver.get('https://www.saucedemo.com/cart.html')

    def switch_to_checkout(self):
        WebDriverWait(self._driver, 4).until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()