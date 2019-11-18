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

        # Navigate to the second page 
        time.sleep(5)
        paginator = driver.find_element_by_class_name('a-pagination')
        second_page = paginator.find_element_by_xpath('//li[3]/a')
        second_page.click()

        # Select the third item
        time.sleep(5)
        item = driver.find_elements_by_class_name('s-result-item')[2]
        item_link = item.find_element_by_class_name('a-link-normal')
        item_link.click()

        # Assert that the item is able to purchase 
        time.sleep(5)
        if len(driver.find_elements_by_id('add-to-cart-button-ubb')) > 0:
            btn_id = 'add-to-cart-button-ubb'
        else:
            btn_id = 'add-to-cart-button'
        
        assert len(driver.find_elements_by_id(btn_id)) > 0
        button_add_to_cart = driver.find_element_by_id(btn_id)

        assert button_add_to_cart.is_displayed()
        assert button_add_to_cart.is_enabled()


    finally:
        time.sleep(10)
        driver.quit()

