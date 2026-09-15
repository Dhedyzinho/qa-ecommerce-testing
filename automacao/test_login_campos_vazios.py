from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.click("#login-button")
    assert "Username is required" in page.locator("[data-test='error']").inner_text()
    page.screenshot(path="evidence/automacao-tc006-login-campos-vazios.png")