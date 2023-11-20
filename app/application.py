from pages.base_page import Page
from pages.target_cart_page import CartPage
from pages.target_main_page import MainPage
from pages.target_search_results_page import SearchResultsPage
from pages.target_sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.target_cart_page = CartPage(driver)
        self.target_main_page = MainPage(driver)
        self.target_search_results_page = SearchResultsPage(driver)
        self.target_sign_in_page = SignInPage(driver)
