import pytest
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser_name="chrome"):
    """
    Create a Selenium WebDriver instance.
    Detect CI (GitHub Actions) and enable headless mode with proper dependencies.
    """
    headless = os.getenv("GITHUB_ACTIONS", "false").lower() == "true"

    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        })
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        if headless:
            # Classic headless mode for CI
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name.lower() == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-save-password-bubble")
        edge_options.add_argument("--disable-popup-blocking")
        edge_options.add_argument("--inprivate")
        edge_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        })

        if headless:
            edge_options.add_argument("--headless")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")
            edge_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")

    return driver

@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    """
    Pytest fixture to initialize and yield a driver instance per test.
    """
    driver = get_driver(request.param)
    yield driver
    driver.quit()
