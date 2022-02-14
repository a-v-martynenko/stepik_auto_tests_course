from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def reg(self, link):
        
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        inp1 = browser.find_element_by_css_selector(".first_block .first")
        inp1.send_keys("Ivan")
        inp2 = browser.find_element_by_css_selector(".first_block .second")
        inp2.send_keys("Petrov")
        inp3 = browser.find_element_by_css_selector(".first_block .third")
        inp3.send_keys("ip@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        expexted_string = "Congratulations! You have successfully registered!"
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(expexted_string, welcome_text, f"Should be the string '{expexted_string}', got '{welcome_text}'") 

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # Браузер должен закрыться

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.reg(link)

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.reg(link)            

if __name__ == "__main__":
    unittest.main()
