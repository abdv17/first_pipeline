import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.smoke
def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com")
    assert page.title() == "OrangeHRM"