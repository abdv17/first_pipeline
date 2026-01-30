import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_forgot_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com",wait_until="domcontentloaded")
    assert page.get_by_text("Forgot your password?", exact=True).is_visible()