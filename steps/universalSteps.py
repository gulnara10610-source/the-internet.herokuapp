


@allure.step('Check title')
def check_title(self, page, text):
    expect(page.locator("//h1")).to_have_text(text)


@allure.step('Check github link on main page')
def check_github_link_on_main_page(page):
    github_link = page.get_by_role("link", name="Fork me on GitHub")
    expect(github_link).to_be_visible()

@allure.step('Check amount links on main page')
def check_amount_links_on_main_page(page, amount):
    links = page.locator("//li/a")
    expect(links).to_have_count(amount)


