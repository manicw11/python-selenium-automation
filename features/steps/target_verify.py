from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty message shown')
def verify_msg(context):
    text_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert text_result == expected_result, f'Expected text {expected_result} is not present'


@then('Verify Sign In page opens')
def verify_sign_in(context):
    text_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_result = 'Sign into your Target account'
    assert text_result == expected_result, f'Expected text {expected_result} is not present'
