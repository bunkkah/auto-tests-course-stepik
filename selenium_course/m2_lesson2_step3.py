from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num_1 = num1.text
    num2 = browser.find_element_by_id("num2")
    num_2 = num2.text
    number = str(int(num_1) + int(num_2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(number)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)

    browser.quit()
