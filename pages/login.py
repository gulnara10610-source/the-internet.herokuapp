from pages.base_page import BasePage
from widgets.element import Element



class LoginPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.title = Element(selector=self._locators.login.title)
        self.user_name = Element(selector=self._locators.login.user_name)
        self.password = Element(selector=self._locators.login.password)
        self.button_login = Element(selector=self._locators.login.button_login)
        self.alert = Element(selector=self._locators.login.alert)