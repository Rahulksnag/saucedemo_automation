from selenium.webdriver.common.by import By

class InventoryPage:
    add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_buttons)[0].click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()
