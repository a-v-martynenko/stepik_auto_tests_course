from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    z = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) 

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    
finally:
    #Ожидание, чтобы успеть скопировать число из всплывающего окна
    time.sleep(5)
    browser.quit()
    # Браузер должен закрыться
    