# tests/test_window_broken_links.py
import pytest
import requests
from helpers import safe_click

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_window_handling(setup, browser):
    driver = setup
    driver.get("https://demoqa.com/browser-windows")
    button = driver.find_element_by_id("tabButton")
    safe_click(driver, ("id", "tabButton"))

    handles = driver.window_handles
    assert len(handles) > 1

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_broken_links(setup, browser):
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    driver = setup
    driver.get("https://demoqa.com/")
    links = driver.find_elements_by_tag_name("a")
    for link in links:
        url = link.get_attribute("href")
        if url:
            try:
                requests.head(url, verify=False)
            except:
                pass
