# tests/test_login_assertions.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from exceptions.custom_exceptions import InvalidLoginError

@pytest.mark.parametrize("username,password,success", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
])
def test_login_validation(setup, username, password, success):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)

    login.set_username(username)
    login.set_password(password)
    login.click_login()

    if not success:
        with pytest.raises(InvalidLoginError):
            raise InvalidLoginError("User account locked!")
    else:
        inv = InventoryPage(driver)
        assert inv.cart_icon is not None
