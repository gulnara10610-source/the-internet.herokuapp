from playwright.sync_api import Locator, Page
class Element:
    page: Page = None

    def __init__(self, selector: str):
        self.selector = selector

    @allure.step("Check text of element")
    def check_text(self, text: str, page=None):
        expect(self._find(page)).to_have_text(str(text))

    @allure.step("Fill input")
    def fill(self, text, page=None) -> str:
        self.input._find(page=page).fill(str(text))
        return text

    @allure.step("Click element")
    def click(self, page: Page = None, **kwargs) -> None:
        try:
            self._find(page).click(**kwargs)
        except Exception as e:
            raise TimeoutError(f"Error while clicking element {self}: {e}")