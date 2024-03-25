from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShopProductsPage:

    def __init__(self, driver):
        self._driver = driver
        #self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def select_products(self, products):
        for product in products:
            id = product
            WebDriverWait(self._driver, 4).until(EC.element_to_be_clickable((By.ID, id))).click()

    def switch_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()