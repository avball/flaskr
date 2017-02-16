#!/home/adam8287/venv-3.5.2/bin/python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class FlaskrFuncTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # Let user sign in/out w/ creds spec'd in config - only need to support one

    # when user logged in, can add new entries w/ text-only title and some
    # html for text - not bothering to sanitize, user is trusted

    # index page shows all entries in reverse chrono, user can add new ones
    # from there if logged in

    self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
