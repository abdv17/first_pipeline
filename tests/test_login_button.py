import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_username_password(page):
    login = LoginPage(page)
    login.open()
    assert login.login_btn.is_visible()