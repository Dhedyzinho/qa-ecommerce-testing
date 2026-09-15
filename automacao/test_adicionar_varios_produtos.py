from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bike-light")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    assert page.locator(".shopping_cart_badge").inner_text() == "3"
    page.screenshot(path="evidence/automacao-tc007-varios-produtos.png")