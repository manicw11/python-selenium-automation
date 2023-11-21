from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In page opens')
def verify_sign_in(context):
    context.app.target_sign_in_page.verify_sign_in()


@when('Input Username and Password')
def input_credentials(context):
    context.app.target_sign_in_page.input_credentials()


@then('Verify User is logged in')
def verify_login(context):
    context.app.target_sign_in_page.verify_login()
