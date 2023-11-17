from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


AIR_FRYER_TXT = (By.XPATH, "//div[contains(text(),'Cuisinart Air Fryer Toaster Oven')]")


@then('Verify air fryer in cart')
def air_fryer_in_cart(context):
    expected_item_text = 'Cuisinart Air Fryer Toaster Oven Stainless Steel CTOA-122'
    actual_item_text = context.driver.find_element(*AIR_FRYER_TXT).text
    print(actual_item_text)
    assert actual_item_text == expected_item_text, f'Expected item, {expected_item_text}, is not in cart'
