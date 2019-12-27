from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
	input3.send_keys("Ivan@Petrov")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'For_lesson2-2_step8.txt')
	send = browser.find_element_by_css_selector("#file")
	send.send_keys(file_path)
	button = browser.find_element_by_xpath("//button[text()='Submit']")
	button.click()

finally:
	# успеваем скопировать код за 10 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла