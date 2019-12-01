# google test, search by id or name, in this case there's no id on the search box
from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.google.com/')
time.sleep(2)
search_box = driver.find_element_by_name('q')
search_box.send_keys('Jo Bleu')

