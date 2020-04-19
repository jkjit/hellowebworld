import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='module')
def firefox_webdriver():
    print("Running setup web driver fixture")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver


@pytest.fixture(scope='module')
def firefox_close(firefox_webdriver):
    firefox_webdriver.close()


