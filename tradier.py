from playwright.sync_api import sync_playwright, expect
import time


def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://tradier.com")
    time.sleep(3)
    # Create a locator.
    get_started = page.get_by_role("link", name="Login")
    # // Click it.
    expect(get_started).to_have_attribute("href", "https://auth.tradier.com")
    get_started.click()
    time.sleep(5)
    # other actions...
    # browser.close()
    print('hello')
    ## Create a password json file or something to use for password logins

with sync_playwright() as playwright:
    print('hi')
    run(playwright)
