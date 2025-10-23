import pytest
from pages.login_page import LoginPage

def test_login_valid(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.set_username("standard_user")
    login.set_password("secret_sauce")
    login.click_login()
    assert "inventory" in driver.current_url

def test_login_invalid(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.set_username("invalid_user")
    login.set_password("wrong_pass")
    login.click_login()
    assert "Epic sadface" in login.get_error_message()
