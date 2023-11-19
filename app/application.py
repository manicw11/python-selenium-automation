from pages.base_page import Page
from pages.target_main_page import MainPage
from pages.target_search_results_page import SearchResultsPage


class Application:
    def __int__(self, driver):
        self.target_search_results_page = SearchResultsPage(driver)
        self.target_main_page = MainPage(driver)
        self.page = Page(driver)

