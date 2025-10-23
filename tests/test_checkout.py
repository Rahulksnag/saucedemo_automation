from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

def test_checkout_process(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    # --- Login ---
    login = LoginPage(driver)
    login.set_username("standard_user")
    login.set_password("secret_sauce")
    login.click_login()

    # --- Add product to cart ---
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.open_cart()

    # --- Proceed to checkout ---
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    # --- Fill details and finish ---
    checkout = CheckoutPage(driver)
    checkout.fill_details_and_continue("Rahul", "KS", "560064")
    checkout.finish_order()
    checkout.verify_order_completion()
