#test para inputs user y pass

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://newtours.demoaut.com/')
time.sleep(2)
user_box = driver.find_element_by_name('userName')
password_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_name('login')
user_box.send_keys('test')
password_box.send_keys('test')
submit_button.click()
time.sleep(2)
link_registration_form = driver.find_element_by_link_text('REGISTER')
assert link_registration_form.text == 'REGISTER'
assert link_registration_form.tag_name == 'a'
driver.quit()


