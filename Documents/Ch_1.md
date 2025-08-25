# Introduction to Playwright with Python

## What is Playwright?
Playwright is an open-source automation library developed by Microsoft for controlling web browsers programmatically. It allows you to automate tasks like web scraping, testing, and browser-based workflows using a simple, modern API. Playwright supports Python, JavaScript/Node.js, Java, and C#, with the Python binding being particularly popular for its ease of use in scripting and testing.

Playwright interacts with Chromium (Chrome, Edge), Firefox, and WebKit (Safari) browsers, enabling cross-browser automation. It provides a high-level API to perform actions like navigating pages, clicking elements, filling forms, and capturing screenshots, all while handling complex browser behaviors like network interception and device emulation.

## Advantages of Playwright
1. **Cross-Browser Support**: Works with Chromium, Firefox, and WebKit, ensuring consistent behavior across major browsers.
2. **Headless and Headed Modes**: Run browsers invisibly (headless) for CI/CD or visibly (headed) for debugging.
3. **Auto-Waiting**: Automatically waits for elements to be ready before acting, reducing flakiness compared to tools like Selenium.
4. **Modern Web Support**: Handles single-page apps, shadow DOM, and complex JavaScript frameworks effortlessly.
5. **Rich Features**: Supports screenshots, videos, network interception, device emulation, and accessibility testing.
6. **Fast Execution**: Optimized for speed with native browser control, unlike older tools that rely on WebDriver.
7. **Synchronous and Asynchronous APIs**: Python offers both `sync_api` for straightforward scripts and `async` for high-performance, concurrent tasks.
8. **Built-in Test Framework**: Includes `@playwright/test` for robust end-to-end testing.

Compared to Selenium, Playwright is faster, more reliable (due to auto-waiting), and better suited for modern web apps, though it’s younger and has a smaller community.

## Supported Browsers
- **Chromium**: Chrome, Microsoft Edge.
- **Firefox**: Mozilla Firefox.
- **WebKit**: Safari’s rendering engine.
- Playwright installs these browser binaries automatically, ensuring consistent versions.

## Basic Use Cases
1. **Web Scraping**: Extract data from websites (e.g., product prices, news articles).
2. **End-to-End Testing**: Automate user flows to test web applications (e.g., login, checkout).
3. **Browser Automation**: Perform repetitive tasks like form submissions or report generation.
4. **Screenshot/Video Capture**: Generate visual outputs for debugging or documentation.
5. **API Testing**: Intercept and mock network requests for testing or simulation.

## Hello World Example
Below is a simple Python script using Playwright’s synchronous API to launch a Chromium browser, navigate to a webpage, and print its title.

```python
from playwright.sync_api import sync_playwright

# Start Playwright
with sync_playwright() as p:
    # Launch Chromium browser in headed mode (visible)
    browser = p.chromium.launch(headless=False)
    
    # Create a new browser context (like an incognito session)
    context = browser.new_context()
    
    # Open a new page
    page = context.new_page()
    
    # Navigate to a website
    page.goto("https://example.com")
    
    # Get and print the page title
    title = page.title()
    print(f"Page title: {title}")
    
    # Close the browser
    browser.close()
```

### Explanation
1. **Import**: `sync_playwright` provides the synchronous API for simpler scripting.
2. **Context Manager**: `with sync_playwright()` ensures resources are cleaned up.
3. **Browser Launch**: `p.chromium.launch(headless=False)` starts Chromium visibly. Set `headless=True` for background execution.
4. **Context and Page**: A context isolates sessions (like incognito); a page is a tab.
5. **Navigation**: `page.goto()` loads the URL.
6. **Title**: `page.title()` retrieves the `<title>` of the page.
7. **Cleanup**: `browser.close()` shuts down the browser.

### How to Run
1. Install Playwright:
   ```bash
   pip install playwright
   playwright install
   ```
2. Save the script as `hello_world.py`.
3. Run it: `python hello_world.py`.
4. Expected output: `Page title: Example Domain`.

## Exercise
1. Modify the script to use Firefox (`p.firefox.launch`) instead of Chromium.
2. Change the URL to `https://wikipedia.org` and print the page title.
3. Run in headless mode and observe the difference.
4. Write an async version of the script using `async_playwright` and `await`. Example:
   ```python
   import asyncio
   from playwright.async_api import async_playwright

   async def main():
       async with async_playwright() as p:
           browser = await p.chromium.launch(headless=False)
           page = await browser.new_page()
           await page.goto("https://example.com")
           title = await page.title()
           print(f"Page title: {title}")
           await browser.close()

   asyncio.run(main())
   ```

## Next Steps
- Explore the [Playwright Python Docs](https://playwright.dev/python/docs/intro) for detailed API references.
- Try navigating to a dynamic site (e.g., a news site) and extract text from an element.
- Move to the next lesson on installation and setup to solidify your environment.

This covers the basics of Playwright! Use the exercise to practice, and refer to the official documentation for deeper exploration.