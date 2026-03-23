def test_checkout_button(page):
    page.goto("https://example.com")

    # Simulate navigation to a fake checkout page
    page.goto("https://example.com")

    # Intentional bug: wrong selector
    page.click("more")

    assert "Example" in page.title()
