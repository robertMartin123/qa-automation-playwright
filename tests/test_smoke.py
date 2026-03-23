import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
"""
Smoke tests:
- Fast
- Critical path only
- Must pass before deeper testing
"""



@pytest.mark.smoke

#def test_homepage_main_heading_is_visible(home_page):

def test_example_domain_homepage_heading(home_page):
    home_page.has_main_heading("Example Domain")


@pytest.mark.regression
@pytest.mark.ui
def test_homepage_does_not_show_login(home_page):
    assert home_page.page.get_by_text("Login").count() == 0

@pytest.mark.exploratory
def test_heading_contains_domain(home_page):
    home_page.open()
    home_page.is_loaded()
    text = home_page.get_main_heading_text()
    assert "Domain" in text





    """
def test_example_domain_homepage_heading(home_page):
    home_page.open()
    home_page.is_loaded()
    home_page.has_main_heading("Example Domain")


"""


"""
def test_homepage_main_heading_is_visible(page: Page):
    home = HomePage(page)
    home.open()

    assert home.has_main_heading("Example Domain")

"""

"""
@pytest.mark.regression
def test_homepage_does_not_show_login(page: Page):
    home = HomePage(page)
    home.open()

    assert page.get_by_text("Login").count() == 0
"""



