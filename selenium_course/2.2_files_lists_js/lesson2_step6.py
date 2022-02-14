from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:     
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.execute_script("window.scrollBy(0,150);")
    
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    ch_box = browser.find_element_by_id("robotCheckbox")
    ch_box.click()

    r_btn = browser.find_element_by_id("robotsRule")
    r_btn.click()

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    
finally:
    #Ожидание, чтобы успеть скопировать число из всплывающего окна
    time.sleep(5)
    browser.quit()
    # Браузер должен закрыться
    