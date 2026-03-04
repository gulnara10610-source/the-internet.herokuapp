import pytest
from playwright.sync_api import sync_playwright
from steps.steps import Steps
from pages.pages import Pages
from widgets.element import Element


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            "--disable-save-password-bubble",  # Отключает всплывающее окно сохранения пароля
            "--disable-notifications", # Отключает системные уведомления
            "--disable-features=Translate"
        ]

    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        viewport={"width": 1440, "height": 1024},
        locale="en-US"
    )
    page = context.new_page()
    page.set_default_timeout(60000)
    yield page
    page.close()
    context.close()

@pytest.fixture(autouse=True)
def set_element_page(page):
    Element.page = page

@pytest.fixture(scope="session", autouse=True)
def pages():
    return Pages()

@pytest.fixture(scope="session", autouse=True)
def steps(pages):
    """Фикстура для получения экземпляра Steps"""
    return Steps(pages)
