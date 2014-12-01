import os
from selenium import webdriver
import unittest

chromedriver = "G:\SoftAndIT\DRIVERS\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()

#chromedriver = "G:\SoftAndIT\DRIVERS\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)
#driver.get("http://localhost:8000")