from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
try:     
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    
    btn1 = browser.find_element_by_id("book")
    btn1.click()

    x = browser.find_element_by_id("input_value").text        
    y = calc(x)
    
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    btn2 = browser.find_element_by_css_selector("button[type='submit']")
    btn2.click()
    
finally:
    #Ожидание, чтобы успеть скопировать число из всплывающего окна
    time.sleep(10)
    browser.quit()
    # Браузер должен закрыться
    