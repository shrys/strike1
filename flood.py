import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get(('https://shrysg.sarahah.com/'))

text = 'test_text'

textArea = driver.find_elements_by_tag_name('textarea')

textArea.send_keys("This text is send using Python code.")

#String textagain = text.getAttribute("value");
#username.send_keys(usernameStr)
#print (text)

