import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Pages.PageIndex import *
from Pages.FlightPage import *
from Pages.PageRegister import *
import sys
import xmlrunner
import HtmlTestRunner
from helpers.data import *


class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://newtours.demoaut.com/')
        # self.driver.maximize_window()
        self.driver.set_window_size(400, 400)
        self.page_index = PageIndex(self.driver)
        self.page_flight = FlightPage(self.driver)
        self.page_register = PageRegister(self.driver)

    def test_dropdown(self):
        my_data = test_data()
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value('11')
        self.page_flight.select_country_by_name(my_data.country)
        self.page_flight.verify_country('CONGO')
        self.page_flight.verify_not_country('ITALY')

    def test_register(self):
        self.page_index.login('test', 'test')
        self.page_register.verify_registration_form()

    def test_login_by_tabs(self):
        self.page_index.login_by_tab('test', 'test')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='myreport'))








