import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_loads_successfully(home_page):
    """Verify the homepage opens and the main heading is visible."""
    home_page.open()
    home_page.is_loaded()

    assert home_page.page.locator("h1").is_visible()


@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_heading_text_contains_expected_value(home_page):
    """Verify the homepage heading text contains the expected value."""
    home_page.open()
    home_page.is_loaded()

    heading_text = home_page.get_main_heading_text()
    assert heading_text
    assert "Example Domain" in heading_text


@pytest.mark.regression
@pytest.mark.ui
def test_homepage_does_not_show_login_link(home_page):
    """Verify the homepage does not expose a login link on the landing page."""
    home_page.open()
    home_page.is_loaded()

    assert home_page.page.get_by_text("Login").count() == 0
