from retry import retry
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By

from BaseApp import BasePage


class Locators:
    """
    Class for locators definition.
    """
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, 'button--kLczM')
    LOCATOR_MENU_BUTTON = (By.CLASS_NAME, 'menu-button--7MO72')
    LOCATOR_USERNAME_FIELD = (By.NAME, 'username')
    LOCATOR_PASSWORD_FIELD = (By.NAME, 'password')
    LOCATOR_LOGIN_PAGE_LOGIN_BUTTON = (By.CLASS_NAME, 'Button--3Qzp7')
    LOCATOR_MENU_TOGGLE = (By.CLASS_NAME, 'menu__btn--12YOl')
    LOCATOR_ANALYTICS_BUTTON = (By.XPATH, '//*[@id="sidebarPopover"]/div[1]/div[1]/button')
    LOCATOR_STATISTICS_BUTTON = (By.CLASS_NAME, 'subGroupItem--1jIwu')
    LOCATOR_RUN_REPORT_BUTTON = (By.XPATH,
                                 '//*[@id="scroll-container"]/div[1]/div[2]/form/div/div/div/div[4]/div[2]/button')
    LOCATOR_ROW_LIMIT_FIELD = (By.XPATH,
                               '//*[@id="scroll-container-toolbar"]/div[4]/div/div[1]/div[5]/div[1]/div/div[2]/input')
    LOCATOR_ROW_LIMIT_FIELD_IN_MENU = (By.XPATH,
                                       '//*[@id="scroll-container-toolbar"]/div[8]/div/div[1]/div/div[2]/input')
    LOCATOR_CLICKS_TABLE_VALUE = (By.XPATH,
                                  '//*[@id="scroll-container"]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/'
                                  'div[2]/div/div[2]/div/span')
    LOCATOR_TEST_URL = (By.CLASS_NAME, 'url--1isxt')
    LOCATOR_USER_BUTTON = (By.CLASS_NAME, 'user--3nTmC')
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, '//*[@id="main-header"]/div[4]/div/div/div/div[1]/div[2]')
    LOCATOR_TABLE_MENU = (By.XPATH, '//*[@id="scroll-container-toolbar"]/div[4]/div/label')


class MainHelper(BasePage):
    """
    Class described methods for main page.
    """

    def click_on_the_log_in_button(self):
        return self.find_element(Locators.LOCATOR_LOGIN_BUTTON, time=5).click()

    def click_on_the_menu_button(self):
        return self.find_element(Locators.LOCATOR_MENU_BUTTON, time=5).click()


class LoginHelper(BasePage):
    """
    Class described methods for login page
    """

    def enter_username(self, username: str):
        username_field = self.find_element(Locators.LOCATOR_USERNAME_FIELD)
        username_field.click()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        username_field = self.find_element(Locators.LOCATOR_PASSWORD_FIELD)
        username_field.click()
        username_field.send_keys(password)

    def click_on_the_log_in_button(self):
        return self.find_element(Locators.LOCATOR_LOGIN_PAGE_LOGIN_BUTTON, time=2).click()


class OverviewHelper(BasePage):
    """
    Class described methods for overview page.
    """

    def click_on_the_menu_toggle(self):
        return self.find_element(Locators.LOCATOR_MENU_TOGGLE, time=5).click()

    @retry(ElementNotInteractableException, tries=10, delay=1)
    def click_on_the_analytics_button(self):
        return self.find_element(Locators.LOCATOR_ANALYTICS_BUTTON, time=8).click()

    def click_on_the_statistics_button(self):
        return self.find_element(Locators.LOCATOR_STATISTICS_BUTTON, time=5).click()

    @retry(ElementClickInterceptedException, tries=10, delay=1)
    def click_on_the_run_report_button(self):
        button = self.find_element(Locators.LOCATOR_RUN_REPORT_BUTTON, time=8)
        return self.driver.execute_script("arguments[0].click();", button)

    def enter_value_to_row_limit_field(self, value: str):
        row_limit_field = self.find_element(Locators.LOCATOR_ROW_LIMIT_FIELD)
        row_limit_field.click()
        row_limit_field.send_keys(value)
        return row_limit_field

    def enter_value_to_row_limit_field_in_menu(self, value: str):
        row_limit_field = self.find_element(Locators.LOCATOR_ROW_LIMIT_FIELD_IN_MENU)
        row_limit_field.click()
        row_limit_field.send_keys(value)
        return row_limit_field

    def get_clicks_value(self):
        clicks_element = self.find_element(Locators.LOCATOR_CLICKS_TABLE_VALUE)
        return clicks_element.text

    def get_test_locator(self):
        return self.find_element(Locators.LOCATOR_TEST_URL).text

    def click_on_the_user_button(self):
        return self.find_element(Locators.LOCATOR_USER_BUTTON, time=5).click()

    @retry(ElementNotInteractableException, tries=10, delay=1)
    def click_on_the_logout_button(self):
        return self.find_element(Locators.LOCATOR_LOGOUT_BUTTON, time=5).click()

    def click_on_the_table_menu_button(self):
        return self.find_element(Locators.LOCATOR_TABLE_MENU, time=8).click()
