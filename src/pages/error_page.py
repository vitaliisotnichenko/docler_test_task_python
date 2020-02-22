
from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ErrorPage(BasePage):

    def is_click_at_the_error_item(self):
        self.is_click_at_the_item((By.CSS_SELECTOR, "#error")).click()

    def title_at_page(self):
        return self.browser.title