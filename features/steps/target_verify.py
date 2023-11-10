from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify cart is empty message shown')
def verify_msg(context):
    text_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert text_result == expected_result, f'Expected text {expected_result} is not present'


@when('Click on Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click on Menu Sign In')
def click_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In page opens')
def verify_sign_in(context):
    text_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_result = 'Sign into your Target account'
    assert text_result == expected_result, f'Expected text {expected_result} is not present'
