from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CalculatorMainPage:

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def time_of_delay(self, delay):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    def input_exemple(self, xpath_value1, xpath_sign, xpath_value2):
        self._driver.find_element(By.XPATH, xpath_value1).click()
        self._driver.find_element(By.XPATH, xpath_sign).click()
        self._driver.find_element(By.XPATH, xpath_value2).click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    def check_result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return (result)
