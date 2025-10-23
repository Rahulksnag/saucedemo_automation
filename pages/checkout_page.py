from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_details_and_continue(self, fname, lname, pincode):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(pincode)
        self.driver.find_element(*self.continue_button).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def verify_order_completion(self):
        confirmation_msg = (By.CLASS_NAME, "complete-header")
        msg_text = self.wait.until(EC.visibility_of_element_located(confirmation_msg)).text
        assert "Thank you for your order!" in msg_text
