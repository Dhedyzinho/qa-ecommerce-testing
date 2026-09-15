from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "senha_errada")
        page.click("#login-button")
        assert "Username and password do not match" in page.locator("[data-test='error']").inner_text()
        page.screenshot(path="evidence/automacao-tc002-login-invalido.png")
        browser.close()