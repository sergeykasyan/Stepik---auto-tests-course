from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

#def calc(x):
	#return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	a = browser.find_element_by_css_selector("#num1").text
	b = browser.find_element_by_css_selector("#num2").text
	select = Select(browser.find_element_by_css_selector("#dropdown"))
	select.select_by_value(str(int(a) + int(b)))
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()

# не забываем оставить пустую строку в конце файла