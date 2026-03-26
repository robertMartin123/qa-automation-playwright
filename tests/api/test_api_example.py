import pytest

@pytest.fixture
def api_request_context(playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()
