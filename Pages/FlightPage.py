
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class FlightPage:
    def __init__(self, myDriver):
        self.driver = myDriver

    def select_country_by_index(self, index):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        countryDropdown.select_by_index(index)

    def select_country_by_value(self, value):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        countryDropdown.select_by_value(value)

    def select_country_by_name(self, name):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        countryDropdown.select_by_visible_text(name)

    def verify_country(self, country):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        self.assertEqual(countryDropdown.first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        self.assertNotEqual(countryDropdown.first_selected_option.text.strip(), country)



