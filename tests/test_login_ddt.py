import pytest
from tests.data.test_data import get_login_data

@pytest.mark.ddt
@pytest.mark.parametrize("username,password", get_login_data())
def test_login_data_driven(page, config, username, password):
    page.goto(config.BASE_URL)

    # Simulate login steps (replace with real locators later)
    print(f"Testing login with {username} / {password}")

    assert username is not None  # placeholder assertion
