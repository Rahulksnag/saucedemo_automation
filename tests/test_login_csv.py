import pytest
from pages.login_page import LoginPage
from utilities.read_csv import read_csv

# Load CSV data
login_data = read_csv("./test_data/login_data.csv")

@pytest.mark.parametrize("user", login_data)
def test_login_csv(setup, user):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.set_username(user["username"])
    login.set_password(user["password"])
    login.click_login()

    if user["username"] == "standard_user":
        # Valid login should go to inventory
        assert "inventory" in driver.current_url
    else:
        # Invalid or locked users should see Epic sadface error
        assert "Epic sadface" in login.get_error_message()
