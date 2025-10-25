# utilities/custom_exceptions.py
class ElementNotVisibleError(Exception):
    """Raised when an expected element is not visible on the page."""
    pass

class InvalidTestDataError(Exception):
    """Raised when test data was invalid or inconsistent."""
    pass
