# pages/demoqa_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoQAElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # All 8 locators examples
        self.all_locators = [
            (By.ID, "simpleLink"),
            (By.NAME, "exampleName"),
            (By.XPATH, "//a[text()='Home']"),
            (By.CSS_SELECTOR, "a#simpleLink"),
            (By.CLASS_NAME, "home-banner"),
            (By.TAG_NAME, "a"),
            (By.LINK_TEXT, "Home"),
            (By.PARTIAL_LINK_TEXT, "Hom")
        ]

class DemoQADragDropPage:
    def __init__(self, driver):
        self.driver = driver
        self.draggable = driver.find_element(By.ID, "draggable")
        self.droppable = driver.find_element(By.ID, "droppable")

    def droppable_element(self):
        return self.droppable

class DemoQAFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Radio buttons
        self.radio_male = (By.ID, "gender-radio-1")
        self.radio_female = (By.ID, "gender-radio-2")
        self.radio_other = (By.ID, "gender-radio-3")

        # Checkboxes
        self.hobbies_checkboxes = [
            (By.ID, "hobbies-checkbox-1"),
            (By.ID, "hobbies-checkbox-2"),
            (By.ID, "hobbies-checkbox-3")
        ]

        # Dropdowns
        self.state_dropdown = (By.ID, "state")
        self.city_dropdown = (By.ID, "city")

        # Alerts / modals
        self.alert_button = (By.ID, "alertButton")
        self.confirm_button = (By.ID, "confirmButton")
        self.prompt_button = (By.ID, "promtButton")

        # JS executor / scroll example
        self.submit_button = (By.ID, "submit")

    # Radio buttons
    def select_radio(self, gender="male"):
        if gender.lower() == "male":
            self.driver.find_element(*self.radio_male).click()
        elif gender.lower() == "female":
            self.driver.find_element(*self.radio_female).click()
        else:
            self.driver.find_element(*self.radio_other).click()

    # Dropdowns
    def select_state(self, state_name):
        select = Select(self.driver.find_element(*self.state_dropdown))
        select.select_by_visible_text(state_name)

    def select_city(self, city_name):
        select = Select(self.driver.find_element(*self.city_dropdown))
        select.select_by_visible_text(city_name)

    # Alerts
    def handle_alert(self, alert_type="alert", text=None):
        if alert_type == "alert":
            self.driver.find_element(*self.alert_button).click()
            self.driver.switch_to.alert.accept()
        elif alert_type == "confirm":
            self.driver.find_element(*self.confirm_button).click()
            self.driver.switch_to.alert.dismiss()
        elif alert_type == "prompt":
            self.driver.find_element(*self.prompt_button).click()
            alert = self.driver.switch_to.alert
            alert.send_keys(text or "")
            alert.accept()

    # Hover
    def hover_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # JS executor
    def click_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Scroll
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Broken links
    def get_all_links(self):
        return self.driver.find_elements(By.TAG_NAME, "a")
