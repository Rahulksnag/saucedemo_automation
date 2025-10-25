# tests/test_actions_demoqa.py
import pytest
from pages.demoqa_page import DemoQADragDropPage
from helpers import drag_and_drop_html5

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_drag_and_drop(setup, browser):
    driver = setup
    driver.get("https://demoqa.com/droppable")
    page = DemoQADragDropPage(driver)

    drag_and_drop_html5(driver, page.draggable, page.droppable)
    text = page.droppable_element().text
    assert "Dropped!" in text
