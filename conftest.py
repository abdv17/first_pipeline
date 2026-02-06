import base64
import os
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join("screenshots", file_name)

            page.screenshot(path=screenshot_path,full_page=True)
            with open(screenshot_path, "rb") as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode()

            extra = getattr(rep, "extra", [])
            extra.append(extras.image(image_base64, mime_type="image/png"))
            rep.extra = extra




def pytest_addoption(parser):
    parser.addoption("--ui-browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="qa")

def browser_name(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def browser(browser_name):
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
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

