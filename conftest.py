import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
