

import pytest
from global_scope import url_ui
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage
from src.pages.form_page import FormPage
from src.pages.error_page import ErrorPage
import requests

class TestTaskDocler:

        @pytest.mark.moderate
        @pytest.mark.parametrize("locator",
                                 [
                                     "#home",
                                     "#site",
                                     "#form",
                                     "#error"
                                 ])
        def test_verify_titles_at_pages(self, browser, locator):
            self.base_page = BasePage(browser)
            self.base_page.open(url_ui)
            self.base_page.is_click_at_the_item(locator)
            self.base_page.is_title_at_page("UI Testing Site")
            assert "UI Testing Site"

        @pytest.mark.moderate
        @pytest.mark.parametrize("locator",
                                 [
                                     "#home",
                                     "#site",
                                     "#form",
                                     "#error"
                                 ])
        def test_verify_company_logo_at_pages(self, browser, locator):
            self.base_page = BasePage(browser)
            self.base_page.open(url_ui)
            self.base_page.is_click_at_the_item(locator)
            assert self.base_page.is_company_logo_at_page()

        @pytest.mark.high
        def test_navigate_to_the_home_page(self, browser):
            self.home_page = HomePage(browser)
            self.home_page.open(url_ui)
            self.home_page.is_click_at_the_item("#home")
            home_page = self.home_page.is_text_displayed_at_the_home_page()
            assert "Welcome to the Docler Holding QA Department" in home_page

        @pytest.mark.low
        def test_home_page_button_status(self, browser):
            self.home_page = HomePage(browser)
            self.home_page.open(url_ui)
            self.home_page.is_click_at_the_item("#home")
            backgound_color = self.home_page.is_get_background_color_at_home_page()
            assert 'rgba(8, 8, 8, 1)' in backgound_color

        @pytest.mark.high
        def test_navigate_to_the_form_page(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            form_page = self.form_page.is_text_displayed_at_the_form_page()
            assert "Form" in form_page

        @pytest.mark.low
        def test_form_page_button_status(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            backgound_color = self.form_page.is_get_background_color_at_form_page()
            assert 'rgba(8, 8, 8, 1)' in backgound_color

        @pytest.mark.high
        def test_response_code_at_error_page(self, browser):
            self.error_page = ErrorPage(browser)
            self.error_page.open(url_ui)
            self.error_page.is_click_at_the_item("#error")
            title = self.error_page.title_at_page()
            assert "404 Error: File not found :-)" in title
            r = requests.get('http://uitest.duodecadits.com/error')
            assert r.status_code == 404

        @pytest.mark.high
        def test_navigate_to_the_home_page_from_ui_testing_button(self, browser):
            self.base_page = BasePage(browser)
            self.base_page.open(url_ui)
            self.base_page.is_click_at_the_item("#site")
            self.home_page = HomePage(browser)
            home_page = self.home_page.is_text_displayed_at_the_home_page()
            assert "Welcome to the Docler Holding QA Department" in home_page


        @pytest.mark.low
        def test_verify_the_text_at_home_page_inside_h1_tag(self, browser):
            self.home_page = HomePage(browser)
            self.home_page.open(url_ui)
            self.home_page.is_click_at_the_item("#home")
            home_page = self.home_page.is_text_displayed_at_the_home_page()
            assert "Welcome to the Docler Holding QA Department" in home_page


        @pytest.mark.low
        def test_verify_the_text_at_home_page_inside_p_tag(self, browser):
            self.home_page = HomePage(browser)
            self.home_page.open(url_ui)
            self.home_page.is_click_at_the_item("#home")
            text_inside_p_tag = self.home_page.is_text_displayed_at_the_home_page_inside_p_tag()
            assert "This site is dedicated to perform some exercises and demonstrate automated web testing." in text_inside_p_tag

        @pytest.mark.high
        def test_form_page_contains_one_input_field_and_one_sumbit_button(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.is_input_field_at_the_page()
            submit_button = self.form_page.is_submit_button_at_the_page()
            assert "Go!" in submit_button.text

        @pytest.mark.high
        def test_send_the_form_at_the_form_page(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.fill_input_field("Vitalii")
            self.form_page.click_submit_button_at_the_page()
            assert "Hello Vitalii!" in self.form_page.text_after_submit_form_at_page()
            assert 'hello.html' in self.form_page.is_current_url()

        @pytest.mark.high
        def test_send_the_form_at_the_form_page_with_empty_input_field(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.click_submit_button_at_the_page()
            assert "Hello !" in self.form_page.text_after_submit_form_at_page()
            assert 'hello.html' in self.form_page.is_current_url()


        @pytest.mark.low
        def test_send_the_form_at_the_form_page_with_double_name(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.fill_input_field("Luis Alberto")
            self.form_page.click_submit_button_at_the_page()
            assert "Hello Luis Alberto!" in self.form_page.text_after_submit_form_at_page()
            assert 'hello.html' in self.form_page.is_current_url()

        @pytest.mark.high
        def test_send_the_form_at_the_form_page_with_special_letter_from_other_alphabets(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.fill_input_field("öäro")
            self.form_page.click_submit_button_at_the_page()
            assert "Hello öäro!" in self.form_page.text_after_submit_form_at_page()
            assert 'hello.html' in self.form_page.is_current_url()

        @pytest.mark.high
        def test_send_the_form_at_the_form_page_with_spaces_at_the_name(self, browser):
            self.form_page = FormPage(browser)
            self.form_page.open(url_ui)
            self.form_page.is_click_at_the_item("#form")
            self.form_page.fill_input_field("  Vitalii")
            self.form_page.click_submit_button_at_the_page()
            assert "Hello Vitalii!" in self.form_page.text_after_submit_form_at_page()
            assert 'hello.html' in self.form_page.is_current_url()