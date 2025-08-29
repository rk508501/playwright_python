import pytest
from playwright.sync_api import sync_playwright

def test_navigate_and_assert_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in headed mode
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        page.wait_for_timeout(3000)
        assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"
        browser.close()