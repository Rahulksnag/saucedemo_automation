# conftest.py
import pytest
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pathlib import Path

def get_driver(browser_name="chrome"):
    headless = os.getenv("GITHUB_ACTIONS", "false").lower() == "true" or os.getenv("JENKINS_HOME") is not None

    if browser_name.lower() == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
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
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name.lower() == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-popup-blocking")
        edge_options.add_argument("--inprivate")
        if headless:
            edge_options.add_argument("--headless=new")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")
            edge_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Browser '{browser_name}' is not supported")

    return driver

@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()

# temp file fixture
@pytest.fixture
def temporary_file(tmp_path):
    file_path = tmp_path / "temp_test_file.txt"
    content = "temporary test content"
    file_path.write_text(content)
    yield str(file_path)
    # tmp_path cleanup by pytest automatically

# helper fixture to create screenshots directory
@pytest.fixture(scope="session", autouse=True)
def screenshots_dir():
    d = Path.cwd() / "reports" / "screenshots"
    d.mkdir(parents=True, exist_ok=True)
    return str(d)
