from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

def accept_alert(driver, timeout=5):
    """Accepts browser alert if it appears."""
    import time
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            alert = Alert(driver)
            alert_text = alert.text
            print(f"Alert detected: {alert_text}")
            alert.accept()
            print("Alert accepted.")
            return True
        except NoAlertPresentException:
            time.sleep(0.5)
    return False
