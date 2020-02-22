import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Fixtures
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     browser.implicitly_wait(10)
    yield browser
    browser.quit()



