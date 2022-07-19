"""
Blackberry Google project by Ali Kholafaei
"""


from page_objects.home_page import GoogleHomePage
from page_objects.search_result_page import SearchResultPage
from utilities.base_class import BaseClass
from utilities.text_file_parser import DataParser


class TestGoogleSearch(BaseClass):
    """
    o Search Google for each search phrase
    o Print out the total number of results
    o Print out the URL for the result number listed
    """

    def test_google(self):

        google_home_page = GoogleHomePage(self.driver)
        search_filed  = google_home_page.get_search_field()
        # Parse the test data file
        test_data_parser = DataParser()
        search_dct = test_data_parser.get_test_data()
        search_result_page = SearchResultPage(self.driver)

        # 1- Search Google for each search phrase
        for key, value in search_dct.items():
            google_home_page.set_element_value(search_filed, key)
            google_home_page.submit_element(search_filed)
            # 2 - Get the total number of results
            total = search_result_page.get_total_number_of_search_result()
            # 3- Get URL for the result number listed
            url = search_result_page.get_all_result_url()[int(value)-1]

            # Print out the result and url
            print("\nTotal {0} search result number of is: ".format(key), total)
            print("\nThe url is:", url.get_attribute("href"))
            self.driver.back()




