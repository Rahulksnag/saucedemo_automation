from selenium.webdriver.common.by import By

class ConfirmationPage:
    confirmation_msg = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_msg).text
