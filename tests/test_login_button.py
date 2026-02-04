import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke
def test_login_username_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com",wait_until="domcontentloaded")
    assert page.get_by_role('button',name='Login').is_visible()