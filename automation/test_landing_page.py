import selenium.webdriver
from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import pytest


class TestLandingPage():

    def test_check_title(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        url = "http://localhost:8085"
        driver = self.driver
        driver.get(url)
        print("Web Page title is : {}".format(driver.title))
        assert "Hello World" == driver.title
        driver.close()

    def test_check_content(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        url = "http://localhost:8085"
        driver = self.driver
        driver.get(url)
        assert "12Apr2020" in driver.page_source
        driver.close()

# if __name__ == '__main__':
#     main()
