import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login('Admin', 'admin123')
    page.wait_for_selector('button[type="submit"]')
    assert 'dashboard' in page.url.lower()