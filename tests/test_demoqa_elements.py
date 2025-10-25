# tests/test_demoqa_elements.py
import pytest
from pages.demoqa_page import DemoQAFormPage
from helpers import safe_click

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_checkbox_and_dropdown(setup, browser):
    driver = setup
    driver.get("https://demoqa.com/automation-practice-form")
    page = DemoQAFormPage(driver)

    # Checkbox safe click
    for checkbox in page.hobbies_checkboxes:
        safe_click(driver, checkbox)

    # Dropdown select
    page.select_state("NCR")
    page.select_city("Delhi")
