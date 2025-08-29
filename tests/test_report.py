from playwright.sync_api import sync_playwright
import os

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Example test: Navigate to a website and check title
        page.goto("https://example.com")
        assert "Example Domain" in page.title()

        # Clean up
        page.wait_for_timeout(3000)
        context.close()
        browser.close()
    print("Test passed!")

if __name__ == "__main__":
    # Set the environment variable to enable HTML reporter
    os.environ["PLAYWRIGHT_HTML_REPORT"] = "test-report.html"

    try:
        run_tests()
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")