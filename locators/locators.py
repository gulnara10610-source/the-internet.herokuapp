from locators.login import LoginLocators
from locators.secure import SecureLocators


class Locators:
    def __init__(self) -> None:
        self.login = LoginLocators()
        self.secure = SecureLocators()
