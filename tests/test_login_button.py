import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.mark.regression
def test_login_username_password(page):
    login = LoginPage(page)
    login.open()
    assert login.is_login_visible()