from pages.home_page import HomePage

def test_homepage(page, config):
    home = HomePage(page, config)
    home.go_to()

    assert False
