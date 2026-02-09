import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_forgot_password(page):
    login = LoginPage(page)
    login.open()
    assert page.get_by_text("Forgot your password?", exact=True).is_visible()