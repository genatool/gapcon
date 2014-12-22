__author__ = 'genaroguerrero'
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_python_org_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("some text")
        elem.send_keys(" and some", Keys.ARROW_DOWN)
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()