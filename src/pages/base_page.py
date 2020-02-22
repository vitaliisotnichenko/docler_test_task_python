import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def is_click_at_the_item(self, locator):
        self.browser.find_element(By.CSS_SELECTOR, locator).click()


    def is_title_at_page(self, title):
        assert title in self.browser.title

    def is_company_logo_at_page(self):
        logo = self.browser.find_element(By.CSS_SELECTOR, "#dh_logo")
        return logo.is_displayed()

    def is_current_url(self):
        return self.browser.current_url





