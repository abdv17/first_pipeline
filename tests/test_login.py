from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        page.goto("https://google.com")
        print(page.title())