from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    SIGN_IN_TXT = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in(self):
        text_result = self.find_element(*self.SIGN_IN_TXT).text
        expected_result = 'Sign into your Target account'
        assert text_result == expected_result, f'Expected text {expected_result} is not present'
