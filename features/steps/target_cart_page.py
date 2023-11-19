from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


AIR_FRYER_TXT = (By.XPATH, "//div[contains(text(),'Cuisinart Air Fryer Toaster Oven')]")


@then('Verify air fryer in cart')
def verify_air_fryer_in_cart(context):
    expected_item_text = 'Cuisinart Air Fryer Toaster Oven Stainless Steel CTOA-122'
    actual_item_text = context.driver.find_element(*AIR_FRYER_TXT).text
    print(actual_item_text)
    assert actual_item_text == expected_item_text, f'Expected item, {expected_item_text}, is not in cart'


@then('Verify cart is empty message shown')
def verify_empty_cart_msg(context):
    text_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert text_result == expected_result, f'Expected text {expected_result} is not present'

