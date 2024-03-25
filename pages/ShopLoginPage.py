from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ShopLoginPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def login(self, user_name, password):
        self._driver.find_element(By.ID, "user-name").send_keys(user_name)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()




