from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FormMainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def input_form(self, fname, lname, addr, mail, phone, code, city, coutr, jobpos, company):
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(fname)
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(lname)
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(addr)
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(mail)
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(coutr)
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(jobpos)
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

    def take_color_element(self, locator):
        color_element = self._driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property('Color')
        return(color_element)

    def take_colors_elements_wo_element(self, locator):
        colors_elemnts = self._driver.find_elements(By.CSS_SELECTOR, locator)
        color_list = list()
        for color_element in colors_elemnts:
            color_list.append(color_element.value_of_css_property('Color'))
        return(color_list)