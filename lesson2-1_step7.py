from selenium import webdriver
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element_by_css_selector("#treasure")
	x_value = x_element.get_attribute("valuex")
	y = calc(x_value)
	input1 = browser.find_element_by_css_selector("#answer")
	input1.send_keys(y)
	option1 = browser.find_element_by_css_selector("#robotCheckbox")
	option1.click()
	option1 = browser.find_element_by_css_selector("#robotsRule")
	option1.click()
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()

# не забываем оставить пустую строку в конце файла