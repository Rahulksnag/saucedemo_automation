# tests/test_all_locators.py
import pytest
from pages.demoqa_page import DemoQAElementsPage
from helpers import safe_click

class TestAllLocators:

    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_all_locators(self, setup, browser):
        driver = setup
        driver.get("https://demoqa.com/links")
        page = DemoQAElementsPage(driver)

        # All locators example
        for locator in page.all_locators:
            try:
                safe_click(driver, locator)
            except:
                pass  # ignore non-clickable for demo
