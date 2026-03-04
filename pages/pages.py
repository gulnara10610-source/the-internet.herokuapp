from .login import LoginPage
from .secure import SecurePage



class Pages:
    def __init__(self) -> None:
        self.login = LoginPage()
        self.secure = SecurePage()
