import os
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_name = f"screenshots/{item.name}_{timestamp}.png"
            page.screenshot(path=file_name,full_page=True)



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

