import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke
def test_login_username_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com",wait_until="domcontentloaded")
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("input[name=username]")
    assert page.get_by_placeholder('Username').is_visible()
    assert page.get_by_placeholder('Password').is_visible()