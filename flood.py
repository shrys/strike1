import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
for i in range(0,2):
	driver.get(('https://.sarahah.com/'))
	text = 'test_text'
	driver.find_element_by_xpath(".//*[@id='Text']").send_keys(text)
	driver.find_element_by_xpath(".//*[@id='Send']").click()
