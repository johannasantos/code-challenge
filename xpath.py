from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
# user_box = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[1]/td[2]/input')
pass_box = driver.find_element_by_css_selector('body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=password]')
# pass_box = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input')
submit_button = driver.find_element_by_name('login')
# user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(5)
driver.quit()
