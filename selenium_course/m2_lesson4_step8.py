from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollTo(0, 500)")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)

    browser.quit()
