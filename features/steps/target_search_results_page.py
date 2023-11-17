from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add Cuisinart Air Fryer'][data-test='addToCartButton']")
DECLINE_COVERAGE_BTN = (By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']")
CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@when('Add air fryer to cart')
def add_fryer_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(DECLINE_COVERAGE_BTN))
    context.driver.find_element(*DECLINE_COVERAGE_BTN).click()
    context.driver.find_element(*CART_BTN).click()


