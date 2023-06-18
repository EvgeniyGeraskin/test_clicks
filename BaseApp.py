from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    Class described base methods for working with pages.
    """

    def __init__(self, driver):
        self.driver = driver
        self.original_window = self.driver.current_window_handle

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        return self.driver.get(url)

    def open_new_tab(self):
        self.driver.switch_to.new_window('window')

    def return_to_original_tab(self):
        self.driver.switch_to.window(self.original_window)
