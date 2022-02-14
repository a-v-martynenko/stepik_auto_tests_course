from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"

try:     
    browser = webdriver.Chrome()
    browser.get(link)

    inpName = browser.find_element_by_name("firstname")
    inpName.send_keys("Ivan")

    inpSurame = browser.find_element_by_name("lastname")
    inpSurame.send_keys("Petrov")

    inpEmail = browser.find_element_by_name("email")
    inpEmail.send_keys("ip@mail.ru")

    inpFile = browser.find_element_by_css_selector("*[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'empty.txt')
    inpFile.send_keys(file_path)    

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    
finally:
    #Ожидание, чтобы успеть скопировать число из всплывающего окна
    time.sleep(10)
    browser.quit()
    # Браузер должен закрыться
    