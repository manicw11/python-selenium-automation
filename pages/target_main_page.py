from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def open_main(self):
        self.open_url('https://www.target.com')

    def open_circle(self):
        self.open_url('https://www.target.com/circle')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(5)

    def click_cart(self):
        self.find_element(*self.CART_BTN).click()
        sleep(5)


