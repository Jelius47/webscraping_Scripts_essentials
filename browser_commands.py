# The url of the site to be used 
url = "https://opensource-demo.orangehrmlive.com/"

# Importing ncessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Setting up some configurations

driver = webdriver.Firefox()
driver.get(url=url)

# Creating and loading variables for login creddentials
from dotenv import load_dotenv

# In not best practice
username = "Admin"
pasword = "admin123"
driver.find_element(By.CSS_SELECTOR,value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(2)

driver.back()# goes one step back in a browser history and foward() to a step ahead
time.sleep(2)
driver.refresh()
driver.get_screenshot_as_png()# Gets the screenshot as the binary data "png"

driver.close()# It closes the current window