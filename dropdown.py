# test para dropdowns

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get('http://newtours.demoaut.com/')
time.sleep(2)
driver.find_element_by_link_text('REGISTER').click()
countryDropdown = Select(driver.find_element_by_name('country'))
countryDropdown.select_by_index(5)
countryDropdown.select_by_value('11')
countryDropdown.select_by_visible_text('CONGO')
time.sleep(5)
driver.quit()

