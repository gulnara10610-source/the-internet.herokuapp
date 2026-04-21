import allure
from playwright.sync_api import Locator, Page, expect


class Element:
    page: Page = None

    def __init__(self, selector: str):
        self.input = None
        self.locator = None
        self.selector = selector

    def _find(self) -> Locator:
        if not self.page:
            raise AttributeError("Page не установлена!")
        return self.page.locator(self.selector)

    @allure.step("Check text of element")
    def check_text(self, text: str):
        element = self._find()
        expect(element).to_be_visible()
        expect(element).to_have_text(str(text))

    @allure.step("Fill input")
    def fill(self, text) -> str:
        self._find().fill(str(text))
        return text

    @allure.step("Click element")
    def click(self, **kwargs) -> None:
        self._find().click(**kwargs)

    @allure.step("Check contain text of element")
    def check_contain_text(self, selector: str, text: str):
        element = self.page.locator(selector)
        expect(element).to_contain_text(text)
