#!/usr/bin/python

import webbrowser
import os
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gen

driver = webdriver.Firefox()
for i in range(0,50):
	#digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
	#chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
	driver.get(('https://.sarahah.com/'))
	#text = digits + chars
	filename = "snippet.txt"
	
	markovLength = 5 ##markov length
	gen.buildMapping(gen.wordlist(filename), markovLength)
	text = gen.genSentence(markovLength)

	driver.find_element_by_xpath(".//*[@id='Text']").send_keys(text)
	driver.find_element_by_xpath(".//*[@id='Send']").click()
	time.sleep(5)


