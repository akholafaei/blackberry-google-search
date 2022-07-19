"""
Blackberry Google search project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By


class GoogleSearchLocators:
    # The XPATHs are only the placeholders
    search_field = (By.NAME, "q")

class GoogleHomePage:
    """This class will handle all the interactions with the Google home page"""
    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_search_field(self):
        # * is added to deserialize the tuple of the locator
        return self.driver.find_element(*GoogleSearchLocators.search_field)

    # region setter
    def set_element_value(self, element, value):
        element.send_keys(value)

    # region clicker
    def submit_element(self, element):
        element.submit()



