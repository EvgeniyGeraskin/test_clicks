import os

import pytest
from retry import retry
from selenium.webdriver.chrome.webdriver import WebDriver

from Pages import MainHelper, LoginHelper, OverviewHelper


@pytest.mark.parametrize('resolution', [[1920, 1080], [1366, 768], [1440, 900], [768, 1024]])
def test_clicks(browser, resolution):
    """
    Test for checking +1 clicks functionality.

    :param browser: web driver (e. g. webdriver.Chrome).
    :param resolution: resolution in [width, height] format.
    :return: None.
    """
    browser.set_window_size(resolution[0], resolution[1])
    main_page = MainHelper(browser)
    main_page.go_to_site('https://stripcash.com')
    if resolution[0] < 1024:
        main_page.click_on_the_menu_button()
    main_page.click_on_the_log_in_button()

    login_page = LoginHelper(browser)
    login_page.enter_username(os.environ.get('WEBSITE_LOGIN'))
    login_page.enter_password(os.environ.get('WEBSITE_PASSWORD'))
    login_page.click_on_the_log_in_button()

    overview_page = OverviewHelper(browser)
    st = overview_page.get_test_locator()

    if resolution[0] < 1200:
        overview_page.click_on_the_menu_toggle()
    overview_page.click_on_the_analytics_button()
    overview_page.click_on_the_statistics_button()
    overview_page.click_on_the_run_report_button()
    if resolution[0] < 769:
        overview_page.click_on_the_table_menu_button()
        overview_page.enter_value_to_row_limit_field_in_menu('1')
    else:
        overview_page.enter_value_to_row_limit_field('1')
    clicks = overview_page.get_clicks_value()

    overview_page.open_new_tab()
    overview_page.go_to_site(st)

    overview_page.return_to_original_tab()

    assert_clicks_number(clicks, browser, resolution)

    overview_page.click_on_the_user_button()
    overview_page.click_on_the_logout_button()


@retry(AssertionError, tries=15, delay=10)
def assert_clicks_number(clicks: str, browser: WebDriver, resolution: list):
    """
    Test function for checking clicks number after link for +1 click was clicked.

    :param clicks: number of clicks before link was opened.
    :param browser: web driver (e. g. webdriver.Chrome).
    :param resolution: resolution in [width, height] format.
    :return: None.
    """
    browser.set_window_size(resolution[0], resolution[1])
    overview_page = OverviewHelper(browser)
    overview_page.click_on_the_run_report_button()
    if resolution[0] < 769:
        overview_page.click_on_the_table_menu_button()
        overview_page.enter_value_to_row_limit_field_in_menu('1')
    else:
        overview_page.enter_value_to_row_limit_field('1')
    new_clicks = overview_page.get_clicks_value()
    assert int(new_clicks) - int(clicks) == 1, f'Number of clicks was not changed (or changed more than +1). ' \
                                               f'Was: {clicks}. Now: {new_clicks}'
