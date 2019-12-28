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

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://newtours.demoaut.com/')
        self.page_index = PageIndex(self.driver)
        self.page_flight = FlightPage(self.driver)
        self.page_register = PageRegister(self.driver)

    @unittest.skip("No quiero que se corra el test de registro")
    def test_dropdown(self):
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value('11')
        self.page_flight.select_country_by_name('CONGO')
        self.page_flight.verify_country('CONGO')
        self.page_flight.verify_not_country('ITALY')

    @unittest.skipIf(2>1, "quiero que 1 sea mas que 2")
    def test_register(self):
        self.page_index.login('test', 'test')
        self.page_register.verify_registration_form()

    @unittest.skipUnless(sys.platform.startswith("linux"), "solo es para linux")
    def test_login_by_tabs(self):
        self.page_index.login_by_tab('test', 'test')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='myreport'))








