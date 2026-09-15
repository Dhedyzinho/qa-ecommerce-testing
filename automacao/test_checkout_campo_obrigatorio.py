from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Wesley")
    page.fill("#last-name", "Ferreira")
    page.click("#continue")
    assert "Postal Code is required" in page.locator("[data-test='error']").inner_text()
    page.screenshot(path="evidence/automacao-tc009-campo-obrigatorio.png")
    