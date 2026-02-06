import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
def test_valid_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.open()
    login.login('Admin', 'admin123a')
    assert dashboard.is_dashboard()