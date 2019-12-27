from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time 
import math
#import pyperclip

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	confirm = browser.switch_to.alert
	confirm.accept()
	x = browser.find_element_by_css_selector("#input_value").text
	y = calc(x)
	input_field = browser.find_element_by_css_selector("#answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
	input_field.send_keys(y)
	button = browser.find_element_by_xpath("//button[text()='Submit']")
	button.click()
	#pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])  #для копирования в буфер

finally:
	time.sleep(10)
	browser.quit()

# не забываем оставить пустую строку в конце файла