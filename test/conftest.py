import pytest
from playwright.sync_api import sync_playwright

from pages.pages import Pages
from widgets.element import Element


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=[
            "--disable-save-password-bubble",  # Отключает всплывающее окно сохранения пароля
            "--disable-notifications" # Отключает системные уведомления
        ]
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, locale):
    context = browser.new_context(
        viewport={"width": 1440, "height": 1024},
        locale=locale
    )
    page = context.new_page()
    page.set_default_timeout(3)
    yield page
    page.close()
    context.close()

@pytest.fixture(autouse=True)
def set_element_page(page):
    Element.page = page

@pytest.fixture(scope="session", autouse=True)
def pages():
    return Pages()

