from selenium import webdriver
import time

URL = 'http://www.google.com'
DRIVER_PATH = '/usr/local/bin/chromedriver'
SEARCH_QUERY = "Hellow World."

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome(executable_path=DRIVER_PATH)
        browser.get(URL)
        # browser.find_element_by_css_selector('input[name="q"]').send_keys("Hellow World.")
        search_box = browser.find_element_by_name('q')
        search_box.send_keys(SEARCH_QUERY)
        # browser.find_element_by_css_selector('input[type="submit"').click()
        search_button = browser.find_element_by_name('btnG')
        search_button.submit()
        time.sleep(3)
        titles = browser.find_elements_by_xpath('//h3[@class="r"] ')
        for title in titles:
            print(title.text)
    finally:
        # browser.quit()
        print('exec end')
