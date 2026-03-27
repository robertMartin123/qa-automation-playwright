import pytest


@pytest.mark.hybrid
def test_homepage_and_api(page, config, api_request_context):
    # UI Step
    page.goto(config.BASE_URL)

    assert "Example" in page.title()

    # API Step
    response = api_request_context.get(config.BASE_URL)

    assert response.status == 200
