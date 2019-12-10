from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class PageRegister(object):
    def __init__(self, myDriver):
        self.driver = myDriver
        self.link_registration_form = (By.LINK_TEXT, 'registration form')

    def verify_registration_form(self):
        tc = unittest.TestCase('__init__')
        registration_link = wait(self.driver, 5).until(EC.presence_of_element_located(self.link_registration_form))
        tc.assertEqual(registration_link.text, 'registration form')
