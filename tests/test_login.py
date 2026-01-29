from playwright.sync_api import sync_playwright


def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    assert page.title() == "OrangeHRM"