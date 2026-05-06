def test_base(page):
    page.goto("https://www.google.com")
    assert "Go0ogle" in page.title()