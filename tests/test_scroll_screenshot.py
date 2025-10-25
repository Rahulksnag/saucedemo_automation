# tests/test_scroll_screenshot.py
import pytest
import os
import time
from pages.demoqa_page import DemoQAFormPage

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_scroll_and_screenshot(setup, browser):
    driver = setup
    driver.get("https://demoqa.com/automation-practice-form")
    page = DemoQAFormPage(driver)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    screenshot_path = os.path.join(os.getcwd(), "scroll_screenshot.png")
    driver.save_screenshot(screenshot_path)
    assert os.path.exists(screenshot_path)
