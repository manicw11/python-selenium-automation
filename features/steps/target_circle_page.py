from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')
    sleep(4)