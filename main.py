from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://selenium.dev/")
# If the window of the opened browser is not maximum when opened
browser.maximize_window()# also there is minimize window

# Setting some stuffs just correct 
title = browser.title

assert "Selenium" in title # If not title the program will rise assert error
# useful to check different elements throught our html page
