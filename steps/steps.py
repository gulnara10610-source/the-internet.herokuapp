from pages.pages import Pages
from steps.universalSteps import UniversalSteps


class Steps:
    def __init__(self, pages=None) -> None:
        if pages is None:
            pages = Pages()

        self.universalSteps = UniversalSteps(pages)

