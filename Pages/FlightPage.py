
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By



class FlightPage:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.countryDropdown = (By.NAME, 'country')

    def select_country_by_index(self, index):
        Select(self.driver.find_element(*self.countryDropdown)).select_by_index(index)
        self.driver.get_screenshot_as_file('screenIndex.png')

    def select_country_by_value(self, value):
        Select(self.driver.find_element(*self.countryDropdown)).select_by_value(value)
        self.driver.save_screenshot('screenValue.png')
    def select_country_by_name(self, name):
        Select(self.driver.find_element(*self.countryDropdown)).select_by_visible_text(name)

    def verify_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertEqual(Select(self.driver.find_element(*self.countryDropdown)).first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(Select(self.driver.find_element(*self.countryDropdown)).first_selected_option.text.strip(), country)



