
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class FlightPage:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.countryDropdown = Select(self.driver.find_element_by_name('country'))


    def select_country_by_index(self, index):
        self.countryDropdown.select_by_index(index)

    def select_country_by_value(self, value):
        self.countryDropdown.select_by_value(value)

    def select_country_by_name(self, name):
        self.countryDropdown.select_by_visible_text(name)

    def verify_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertEqual(self.countryDropdown.first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(countryDropdown.first_selected_option.text.strip(), country)



