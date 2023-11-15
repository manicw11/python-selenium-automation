from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Add air fryer to cart')
def add_fryer_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label*='Add Cuisinart Air Fryer'][data-test='addToCartButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


