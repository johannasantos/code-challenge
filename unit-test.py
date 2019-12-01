import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://newtours.demoaut.com/')
        time.sleep(2)

    def test_dropdown(self):
        self.driver.find_element_by_link_text('REGISTER').click()
        countryDropdown = Select(self.driver.find_element_by_name('country'))
        countryDropdown.select_by_index(5)
        countryDropdown.select_by_value('11')
        countryDropdown.select_by_visible_text('CONGO')
        self.assertEqual(countryDropdown.first_selected_option.text.strip(), 'CONGO')

    def test_register(self):
        user_box = self.driver.find_element_by_name('userName')
        password_box = self.driver.find_element_by_name('password')
        submit_button = self.driver.find_element_by_name('login')
        user_box.send_keys('test')
        password_box.send_keys('test')
        submit_button.click()
        time.sleep(2)
        link_registration_form = self.driver.find_element_by_link_text('REGISTER')
        self.assertEqual(link_registration_form.text, 'REGISTER')

    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()


