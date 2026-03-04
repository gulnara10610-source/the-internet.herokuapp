import allure
import pytest
from playwright.sync_api import Page

from pages.pages import Pages
from utils.consts import LOGIN_PAGE
from utils.data import LOGIN_DATA
from utils.texts import *
from utils.users import USER_FOR_TEST


class TestLoginPage:
    @allure.title('Check login with empty Password')
    def test_login_with_empty_password_page(self, page: Page, pages: Pages):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(USER_FOR_TEST.login)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_USERNAME)

    @allure.title('Check login with empty username and password')
    def test_login_with_empty_username_and_password_page(self, page: Page, pages: Pages):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_USERNAME_INVALID)

    @allure.title('Check login with empty username')
    def test_login_with_empty_username_page(self, page: Page, pages: Pages):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.password.fill(USER_FOR_TEST.password)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_USERNAME_INVALID)

    @allure.title('Check login')
    def test_login(self, page: Page, pages: Pages, steps):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(USER_FOR_TEST.login)
        pages.login.password.fill(USER_FOR_TEST.password)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_LOGGED)
        pages.secure.main_title.check_text(SECURE_AREA)
        pages.secure.welcome_title.check_text(WELCOME_TITLE)
        pages.secure.button_logout.check_text(LOGOUT)
        steps.universalSteps.check_github_link_on_main_page(page)
        pages.secure.string_powered_by.check_text(POWERED_BY)
        pages.secure.href_powered_by.check_text(HREF_POWERED_BY)
        pages.secure.button_logout.click()
        pages.login.title.check_text(TITLE_LOGIN_PAGE)

    @pytest.mark.parametrize("username, password, expected_alert", LOGIN_DATA)
    @allure.title('Check login with invalid credentials: username, password')
    def test_login_with_invalid_credentials(self, page: Page, pages: Pages, username, password, expected_alert):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(username)
        pages.login.password.fill(password)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(expected_alert)

