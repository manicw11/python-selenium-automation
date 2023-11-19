from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Add air fryer to cart')
def add_fryer_to_cart(context):
    context.app.target_search_results_page.add_fryer_to_cart()
