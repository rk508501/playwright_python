Below is a detailed sample of Playwright Python tests using the Page Object Model (POM) pattern, which is a best practice for organizing UI test automation code. The POM pattern encapsulates page-specific logic into classes, making tests more maintainable and reusable. The example focuses on a hypothetical login page and includes multiple test scenarios, demonstrating how to structure your Playwright Python project.

The code is organized into a directory structure with page objects and tests, and I’ll provide the content of each file in Markdown format, suitable for importing as `.md` for reference. Each file will be wrapped in an `<xaiArtifact>` tag, and I’ll include a `README.md` to explain the setup and execution. The tests cover basic login functionality, error handling, and navigation, with Playwright’s `sync_api` for simplicity.

---

## Directory Structure
```
playwright_python/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── requirements.txt
└── README.md
```

---

<xaiArtifact artifact_id="9311be49-4814-4e17-9206-1d807752c79d" artifact_version_id="cb212c37-5355-409b-8b81-d4e232dc095b" title="README.md" contentType="text/markdown">

# Playwright Python Page Object Model Example

This project demonstrates Playwright Python tests using the Page Object Model (POM) pattern. It includes sample tests for a hypothetical login page.

## Setup
1. **Install Python**: Ensure Python 3.8+ is installed (`python --version`).
2. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
4. **Run Tests**:
   ```bash
   pytest tests/
   ```

## Structure
- `pages/`: Contains page object classes (e.g., `login_page.py`).
- `tests/`: Contains test cases (e.g., `test_login.py`).
- `requirements.txt`: Lists dependencies.
- `__init__.py`: Makes directories Python packages.

## Notes
- Tests use Playwright’s synchronous API for simplicity.
- Replace `https://example.com/login` with your actual test URL.
- Extend the `LoginPage` class for additional pages (e.g., DashboardPage).

**Further Research Prompt**: "How to extend the Page Object Model in Playwright Python for a multi-page web application, including best practices for handling dynamic locators and integrating with pytest fixtures."

</xaiArtifact>

---

<xaiArtifact artifact_id="ecfb1d43-15f7-446a-8743-54251ab564dc" artifact_version_id="30cc8ec5-69e4-4d12-bff5-8ff9c738b01d" title="requirements.txt" contentType="text/plain">

playwright==1.48.0
pytest==8.3.3
pytest-playwright==0.5.2

</xaiArtifact>

---

<xaiArtifact artifact_id="fd7deeca-e7dc-4a6e-baa1-0724f9b9b42f" artifact_version_id="1c6a4720-3656-43bb-b56e-02c3d3392968" title="pages/login_page.py" contentType="text/python">

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://example.com/login"
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".error-message")

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        """Perform login with given credentials."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def get_error_message(self):
        """Retrieve error message text if present."""
        if self.error_message.is_visible():
            return self.error_message.inner_text()
        return None

    def is_login_successful(self):
        """Check if login was successful by verifying URL change."""
        return "dashboard" in self.page.url

</xaiArtifact>

---

<xaiArtifact artifact_id="20b7812d-c583-466f-85bc-c04cd7196cf5" artifact_version_id="2c585605-b0d0-4d70-96af-6eb69c5eb2c6" title="tests/test_login.py" contentType="text/python">

import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.navigate()
        yield login_page
        browser.close()

def test_successful_login(login_page):
    login_page.login("valid_user", "valid_password")
    assert login_page.is_login_successful(), "Login should redirect to dashboard"

def test_invalid_credentials(login_page):
    login_page.login("invalid_user", "wrong_password")
    error = login_page.get_error_message()
    assert error is not None, "Error message should be displayed"
    assert "Invalid credentials" in error, "Error message should indicate invalid credentials"

def test_empty_fields(login_page):
    login_page.login("", "")
    error = login_page.get_error_message()
    assert error is not None, "Error message should be displayed for empty fields"
    assert "required" in error.lower(), "Error message should mention required fields"

</xaiArtifact>

---

## Explanation of the Code

### Page Object Model (POM)
- **LoginPage Class** (`pages/login_page.py`):
  - Encapsulates the login page’s elements (e.g., `#username`, `#password`) and actions (e.g., `login`, `get_error_message`).
  - Uses Playwright’s `Locator` API for efficient element handling.
  - Methods like `is_login_successful` check outcomes (e.g., URL change after login).

- **Tests** (`tests/test_login.py`):
  - Uses `pytest` with a fixture (`login_page`) to set up the browser and page object for each test.
  - Tests cover:
    - Successful login (checks URL redirect).
    - Invalid credentials (verifies error message).
    - Empty fields (verifies validation error).
  - Assertions ensure expected behavior.

### Key Features
- **Modularity**: The `LoginPage` class separates page logic from tests, making it easy to reuse across test cases.
- **Maintainability**: Update locators in one place (`LoginPage`) if the UI changes.
- **Test Isolation**: The `pytest` fixture ensures each test runs in a fresh browser context.
- **Playwright Integration**: Uses `sync_playwright` for synchronous API, ideal for beginners. (Async API can be explored later for performance.)

### Running the Tests
1. Save the files in the directory structure shown.
2. Follow the `README.md` setup instructions.
3. Run `pytest tests/` to execute the tests.
   - Note: Replace `https://example.com/login` with a real test URL, and adjust locators/credentials to match the actual site.

### Notes
- The tests assume a hypothetical login page with IDs `#username`, `#password`, and a `button[type='submit']`. Update these to match your application.
- The `headless=True` setting runs tests without opening a browser UI, suitable for CI/CD pipelines.
- Extend the POM by adding more page classes (e.g., `DashboardPage`) for other parts of your app.

**Further Research Prompt**: "How to scale the Page Object Model in Playwright Python for large web applications, including strategies for handling dynamic elements, parameterized locators, and integrating with pytest-playwright for cross-browser testing."

---

This sample provides a solid foundation for writing Playwright Python tests with POM. You can import the `.md` files for reference or directly use the Python files in your `playwright_python` repository. If you need help integrating these with your existing project or resolving specific issues (e.g., Git conflicts), let me know!