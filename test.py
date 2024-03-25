import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.FormMainPage import FormMainPage
from pages.CalculatorMainPage import CalculatorMainPage
from pages.ShopLoginPage import ShopLoginPage
from pages.ShopProductsPage import ShopProductsPage
from pages.ShopCartPage import ShopCartPage
from pages.ShopCheckoutPage import ShopCheckoutPage
from pages.ShopTotalCostPage import ShopTotalCostPage

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])


def test_colors_elements():   
    driver = webdriver.Chrome(options=options)
    main_page = FormMainPage(driver)
    main_page.input_form('Sotov', 'Aleskandr', 'Lenina 54-3', 'sotov@mail.ru', '+79818456258', '','Moscow', 'Russia', 'QA', 'SkyPro')
    color_element = main_page.take_color_element('#zip-code')
    colors_elements = main_page.take_colors_elements_wo_element('.alert:not(#zip-code)')
    assert color_element == 'rgb(132, 32, 41)'
    for colors in colors_elements:
        assert colors == 'rgb(15, 81, 50)'

def test_time_of_delay():
    driver = webdriver.Chrome(options=options)
    main_page = CalculatorMainPage(driver)
    delay = 45
    main_page.time_of_delay(delay)
    main_page.input_exemple("//span[text()='7']", "//span[text()='+']", "//span[text()='8']")
    sleep(delay)
    to_be = '15'
    as_is = main_page.check_result()
    assert as_is == to_be

def test_total_cost():
    driver = webdriver.Chrome(options=options)
    main_page = ShopLoginPage(driver)
    main_page.login('standard_user', 'secret_sauce')
    main_page = ShopProductsPage(driver)
    products = ['add-to-cart-sauce-labs-backpack', 'add-to-cart-sauce-labs-bolt-t-shirt', 'add-to-cart-sauce-labs-onesie']
    main_page.select_products(products)
    main_page.switch_to_cart()
    main_page = ShopCartPage(driver)
    main_page.switch_to_checkout()
    main_page = ShopCheckoutPage(driver)
    main_page.checkout('Sotov', 'Aleksandr', '192000')
    main_page.click_to_continue()
    main_page = ShopTotalCostPage(driver)
    as_is = main_page.total_cost()
    to_be = 'Total: $58.29'
    assert as_is == to_be


   
      