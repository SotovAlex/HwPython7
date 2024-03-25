from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShopTotalCostPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def get_page(self):
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')

    def total_cost(self):
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text 
        return(total)
