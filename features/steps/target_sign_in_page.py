from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In page opens')
def verify_sign_in(context):
    context.app.target_sign_in_page.verify_sign_in()
