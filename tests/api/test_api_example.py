import pytest

@pytest.mark.api
def test_get_example_domain(api_request_context):
    response = api_request_context.get("https://example.com")

    assert response.status == 200

