import time

from pytest_bdd import when, parsers, then
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):

    def is_text_displayed_at_the_home_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#home").click()
        return self.browser.find_element(By.CSS_SELECTOR, ".ui-test>h1").text

    def is_text_displayed_at_the_home_page_inside_p_tag(self):
        self.browser.find_element(By.CSS_SELECTOR, "#home").click()
        return self.browser.find_element(By.CSS_SELECTOR, ".ui-test>p").text


    def is_get_background_color_at_home_page(self):
        rgb = self.browser.find_element(By.CSS_SELECTOR, "#home").value_of_css_property("background-color")
        return rgb
