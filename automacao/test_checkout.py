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
    page.fill("#postal-code", "20000-000")
    page.click("#continue")
    assert "checkout-step-two.html" in page.url
    page.click("#finish")
    assert "Thank you for your order!" in page.locator(".complete-header").inner_text()
    page.screenshot(path="evidence/automacao-tc005-checkout.png")