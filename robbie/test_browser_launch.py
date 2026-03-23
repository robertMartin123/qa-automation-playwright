import time

def test_open_browser(page):
    page.goto("https://example.com")

    # wait so we can see the browser
    time.sleep(2)

    assert "Example" in page.title()

d