from pages.base_page import BasePage
from widgets.element import Element


class SecurePage(BasePage):
    def __init__(self) -> None:
        super().__init__()

        self.main_title = Element(selector=self._locators.secure.main_title)
        self.welcome_title = Element(selector=self._locators.secure.welcome_title)
        self.button_logout = Element(selector=self._locators.secure.button_logout)
        self.string_powered_by = Element(selector=self._locators.secure.string_powered_by)
        self.href_powered_by = Element(selector=self._locators.secure.href_powered_by)