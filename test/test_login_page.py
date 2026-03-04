import pages.login
import steps
from config import BASE_URL
from utils.consts import LOGIN_PAGE
from utils.texts import ALERT_USERNAME, SECURE_AREA, WELCOME_TITLE, LOGOUT, POWERED_BY, HREF_POWERED_BY, \
    TITLE_LOGIN_PAGE
from utils.users import USER_FOR_TEST


class TestLoginPage:
    @pytest.fixture(autouse=True)
    def open_login_page(self, page: Page):
        page.goto(LOGIN_PAGE)


    @allure.title('Check login with empty Password')
    def test_login_with_empty_password_page(self, page: Page, pages: Pages):
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(USER_FOR_TEST.login)
        pages.login.button_login.click()
        pages.login.alert.check_text(ALERT_USERNAME)

    @allure.title('Check login with empty username and password')
    def test_login_with_empty_username_and_password_page(self, page: Page, pages: Pages):
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.button_login.click()
        pages.login.alert.check_text(ALERT_USERNAME)

    @allure.title('Check login')
    def test_login(self, page: Page, pages: Pages, steps: Steps):
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(USER_FOR_TEST.login)
        pages.login.password.fill(USER_FOR_TEST.password)
        pages.login.button_login.click()
        pages.login.alert.check_text(ALERT_USERNAME)
        pages.secure.main_title.check_text(SECURE_AREA)
        pages.secure.welcome_title.check_text(WELCOME_TITLE)
        pages.secure.button_logout.check_text(LOGOUT)
        steps.universalSteps.check_github_link_on_main_page()
        pages.secure.string_powered_by.check_text(POWERED_BY)
        pages.secure.href_powered_by.check_text(HREF_POWERED_BY)
        pages.secure.button_logout.click()
        pages.login.title.check_text(TITLE_LOGIN_PAGE)





