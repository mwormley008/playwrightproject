from playwright.sync_api import sync_playwright
import time


def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://tradier.com")
    time.sleep(3)
    # other actions...
    # browser.close()
    print('hello')

with sync_playwright() as playwright:
    print('hi')
    run(playwright)
