import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption("--ui-browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="qa")

def browser_name(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def browser(browser_name):
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)
        else:
            raise ValueError(f'Unsupported browser: {browser_name}')
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport=None)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    return page

