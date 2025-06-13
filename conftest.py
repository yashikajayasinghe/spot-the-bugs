import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

@pytest.fixture(scope="session")
def session_browser_context():
    """Fixture to create a browser context for the entire session."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def session_page(session_browser_context):
    """Fixture to create a page for the entire session."""
    page = session_browser_context.new_page()
    yield page