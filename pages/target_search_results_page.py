from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextId"]')
    CLOSE_SIDE_WNDW_BTN = (By.CSS_SELECTOR, "[class*='styles__CellContent'] [aria-label='close']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def add_product_to_cart(self):
        sleep(5)
        self.click(*self.ADD_TO_CART_BTN)
        sleep(5)
#        self.wait.until(EC.visibility_of_element_located(self.DECLINE_COVERAGE_BTN))
        self.click(*self.CLOSE_SIDE_WNDW_BTN)
        self.click(*self.CART_BTN)
