from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


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
