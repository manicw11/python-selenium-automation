from pages.base_page import Page


class TermsAndConditionsPage(Page):

    def verify_terms_and_conditions_opened(self):
        self.verify_partial_url('https://www.target.com/c/terms-conditions/')
