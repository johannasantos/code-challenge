from selenium import webdriver
import time

def test_amazon_search():
    driver = webdriver.Chrome()
    try:
        # Start Amazon
        driver.get('http://www.amazon.com')
        time.sleep(5)
        # Search 'Alexa'
        searcher = driver.find_element_by_id('twotabsearchtextbox')
        searcher.send_keys('Alexa')
        searcher.submit()

        # Go to the second page 
        time.sleep(5)
        paginator = driver.find_element_by_class_name('a-pagination')
        second_page = paginator.find_element_by_xpath('//li[3]/a')
        second_page.click()








    finally:
        driver.quit()

