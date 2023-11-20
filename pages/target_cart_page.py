from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):
    EMPTY_CART_TXT = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_ITEM = (By.CSS_SELECTOR, "[data-test='cartItem']")

    def verify_empty_cart(self):
        text_result = self.find_element(*self.EMPTY_CART_TXT).text
        expected_result = 'Your cart is empty'
        assert text_result == expected_result, f'Expected text {expected_result} is not present'

    def verify_product_in_cart(self, product):
        expected_item_text = f'{product}'
        actual_item_text = self.find_element(*self.CART_ITEM).text
        print(actual_item_text)
        assert expected_item_text in actual_item_text, f'Expected item, {expected_item_text}, is not in cart'
