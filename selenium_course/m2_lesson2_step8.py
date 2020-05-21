from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("blabla@email.net")

    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)

    browser.quit()