import steps
from config import BASE_URL
from utils.texts import TITILE_MAIN_PAGE


class TestMainPage:
    @allure.title('Check links on main page')
    def test_check_links(self, page, steps):
        page.goto(BASE_URL)
        steps.universalSteps.check_title(TITILE_MAIN_PAGE)
        steps.universalSteps.check_github_link_on_main_page()
        steps.universalSteps.check_amount_links_on_main_page(44)

