import pytest
import os
import datetime
from config.config_loader import get_config

from pages.home_page import HomePage

@pytest.fixture
def home_page(page, config):
    return HomePage(page, config)




@pytest.fixture
def api_request_context(playwright):
    request_context = playwright.request.new_context(
        ignore_https_errors = True
    )


    yield request_context
    request_context.dispose()




# ✅ Config fixture
@pytest.fixture(scope="session")
def config():
    return get_config()


# ✅ Context fixture (with video + tracing)
@pytest.fixture
def context(browser):
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    context.close()


# ✅ Page fixture (override)
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ✅ Hook (screenshots + trace on failure)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        context = item.funcargs.get("context", None)

        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshots/failure_{timestamp}.png"
            page.screenshot(path=file_name)
            print(f"\n📸 Screenshot saved: {file_name}")

        if context:
            context.tracing.stop(path="trace_failed.zip")
            print("\n📦 Trace saved: trace_failed.zip")


