from playwright.sync_api import sync_playwright


def test_login_negative(page):
    page.goto("https://opensource-demo.orangehrmlive.com",wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    assert page.title() == "OrangeHRMa"