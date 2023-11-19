from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target main page')
def open_target_main(context):
    context.app.target_main_page.open_main()


@given('Open Target Circle page')
def open_target_circle(context):
    context.app.target_main_page.open_circle()


@when('Search for {product}')
def input_search_field(context, product):
    context.app.target_main_page.search(product)


@when('Click on cart icon')
def click_cart(context):
    context.app.target_main_page.click_cart()
#    context.driver.wait.until(EC.url_changes('https://www.target.com/cart'))

