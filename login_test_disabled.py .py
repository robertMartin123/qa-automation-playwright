from pages.home_page import HomePage


def test_homepage(page, config):
    print("Starting test_homepage")  # quick visibility

    home = HomePage(page, config)
    home.go_to()

    print("Finished navigation")

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()



def test_homepage(page, config):
    home = HomePage(page, config)
    home.go_to()

    assert False  # force failure

