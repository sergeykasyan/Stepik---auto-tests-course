from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x = browser.find_element_by_css_selector("#input_value").text
	y = calc(x)
	input_field = browser.find_element_by_css_selector("#answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
	input_field.send_keys(y)
	option1 = browser.find_element_by_css_selector("#robotCheckbox")
	option1.click()
	option2 = browser.find_element_by_css_selector("#robotsRule")
	option2.click()
	button = browser.find_element_by_xpath("//button[text()='Submit']")
	button.click()

finally:
	time.sleep(10)
	browser.quit()

# не забываем оставить пустую строку в конце файла