import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_chrome_options() -> Options:
    """
    Sets chrome options for Selenium.

    --no-sandbox and --disable-dev-shm-usage arguments were chosen
    because without them Chrome may crash inside Docker container.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options


@pytest.fixture(scope="session")
def browser():
    """
    Pytest fixture for set up web driver (launch) and tear down web driver (quit).
    :return: web driver (e. g. webdriver.Chrome).
    """
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.maximize_window()
    yield driver
    driver.quit()
