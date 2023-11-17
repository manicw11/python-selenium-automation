from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def input_search_field(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(CART_BTN))


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_BTN).click()
    context.driver.wait.until(EC.url_changes('https://www.target.com/cart'))

