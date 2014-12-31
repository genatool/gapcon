__author__ = 'genaroguerrero'
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class Logintest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com")



    def test_Login(self):
        driver = self.driver
        emailFieldID = "email"
        passFieldID  = "pass"
        loginButtonXpath = "//input[@value='Log In']"


        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonelement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys("jgenarotool@gmail.com")
        passFieldElement.clear()
        passFieldElement.send_keys("Hatred55")
        loginButtonelement.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()