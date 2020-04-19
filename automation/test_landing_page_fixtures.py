def test_check_title(firefox_webdriver):
    driver = firefox_webdriver
    url = "http://localhost:8085"
    driver.get(url)
    print("Web Page title is : {}".format(driver.title))
    assert "Hello World" == driver.title


def test_check_content(firefox_webdriver):
    driver = firefox_webdriver
    url = "http://localhost:8085"
    driver.get(url)
    assert "12Apr2020" in driver.page_source


def test_cleanup(firefox_close):
    print("Closed all open FireFox driver connections")
