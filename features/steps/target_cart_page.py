from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify air fryer in cart')
def air_fryer_in_cart(context):
    expected_item_text = 'Cuisinart Air Fryer Toaster Oven Stainless Steel CTOA-122'
    actual_item_text = context.driver.find_element(By.XPATH, "//div[contains(text(),'Cuisinart Air Fryer Toaster Oven')]").text
    print(actual_item_text)
    assert actual_item_text == expected_item_text, f'Expected item, {expected_item_text}, is not in cart'
