"""
MovieApp project by Ali Kholafaei
"""

import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def setup(request):
    """ Setup and Tear down the driver"""


    driver = webdriver.Chrome(executable_path="C:\\Users\\Solmaz\\Desktop\\chromedriver.exe")
    driver.implicitly_wait(0.5)
    # launch URL
    driver.get("https://www.google.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()