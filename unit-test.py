import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.PageIndex import *
from Pages.FlightPage import *

import time

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://newtours.demoaut.com/')
        self.page_index = PageIndex(self.driver)
        self.page_flight = FlightPage(self.driver)
        time.sleep(2)

    def test_dropdown(self):
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value(11)
        self.page_flight.select_country_by_name('CONGO')
        self.page_flight.verify_country('CONGO')
        self.page_flight.verify_not_country('ITALY')

    def test_register(self):
        self.page_index.login('test', 'test')
        link_registration_form = self.driver.find_element_by_link_text('REGISTER')
        self.assertEqual(link_registration_form.text, 'REGISTER')

    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()


