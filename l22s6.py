from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	xel = browser.find_element_by_id('input_value')
	x = int(xel.text)
	y = calc(x)
	answer = browser.find_element_by_id('answer')
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
	answer.send_keys(y)
	checkbox = browser.find_element_by_id('robotCheckbox')
	browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
	checkbox.click()
	rr = browser.find_element_by_id('robotsRule')
	browser.execute_script("return arguments[0].scrollIntoView(true);", rr)
	rr.click()
	btn = browser.find_element_by_css_selector('.btn')
	browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
	btn.click()
finally:
	time.sleep(10)
	browser.quit()
