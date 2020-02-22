
from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormPage(BasePage):

    def is_text_displayed_at_the_form_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#form").click()
        return self.browser.find_element(By.CSS_SELECTOR, ".ui-test>h1").text

    def is_get_background_color_at_form_page(self):
        rgb = self.browser.find_element(By.CSS_SELECTOR, "#form").value_of_css_property("background-color")
        return rgb

    def is_input_field_at_the_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#hello-input")

    def fill_input_field(self, name):
        self.browser.find_element(By.CSS_SELECTOR, "#hello-input").send_keys(name)

    def click_submit_button_at_the_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "#hello-submit").click()

    def is_submit_button_at_the_page(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#hello-submit")

    def text_after_submit_form_at_page(self):
        submit_form = self.browser.find_element(By.CSS_SELECTOR, "#hello-text")
        return submit_form.text