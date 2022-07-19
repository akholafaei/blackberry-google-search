"""
Blackberry Google search project by Ali Kholafaei
"""

from selenium.webdriver.common.by import By


class SearchResultLocators:
    # The XPATHs are only the placeholders
    result_stats = (By.XPATH, "//div[@id = 'result-stats']")
    result_links = (By.XPATH, "//div[@id='search']//div[@lang='en']//div[@class='yuRUbf']//a")

class SearchResultPage:
    """This class will handle all the interactions with the Search result page"""
    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_total_number_of_search_result(self):
        return self.driver.find_element(*SearchResultLocators.result_stats).text.strip().split(" ")[1]

    def get_all_result_url(self)->list:
        return self.driver.find_elements(*SearchResultLocators.result_links)