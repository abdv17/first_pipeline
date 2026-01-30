from playwright.sync_api import sync_playwright


def test_login_negative(page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    assert page.title() == "OrangeHRMa"