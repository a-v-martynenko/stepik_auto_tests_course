from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:     
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector("button[type='submit']")
    btn1.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    
    y = calc(x)

    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    btn2 = browser.find_element_by_css_selector("button[type='submit']")
    btn2.click()
    
finally:
    #Ожидание, чтобы успеть скопировать число из всплывающего окна
    time.sleep(5)
    browser.quit()
    # Браузер должен закрыться
    