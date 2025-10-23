import os
import tempfile
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser_name="chrome"):
    headless = os.getenv("GITHUB_ACTIONS", "false").lower() == "true"

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        })
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--inprivate")

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser '{browser_name}' not supported")

    return driver

@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    driver = get_driver(request.param)
    yield driver
    driver.quit()

# Attach screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_path = os.path.join(tempfile.gettempdir(), f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
