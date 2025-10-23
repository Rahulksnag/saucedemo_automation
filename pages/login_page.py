from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username = (By.ID, "user-name")
    textbox_password = (By.ID, "password")
    button_login = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*self.textbox_username).clear()
        self.driver.find_element(*self.textbox_username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button_login).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
