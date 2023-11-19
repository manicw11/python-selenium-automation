from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add Cuisinart Air Fryer'][data-test='addToCartButton']")
    DECLINE_COVERAGE_BTN = (By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def add_fryer_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN).click()
        sleep(5)
#        self.wait.until(EC.visibility_of_element_located(self.DECLINE_COVERAGE_BTN))
        self.find_element(*self.DECLINE_COVERAGE_BTN).click()
        self.find_element(*self.CART_BTN).click()
