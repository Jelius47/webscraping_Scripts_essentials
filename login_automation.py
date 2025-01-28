# The url of the site to be used 
url = "https://www.saucedemo.com/v1/"

# Importing ncessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting up some configurations

driver = webdriver.Firefox()
driver.get(url=url)

# Creating and loading variables for login creddentials
from dotenv import load_dotenv

# In not best practice
username = "standard_user"
pasword = "secret_sauce"


# Locating the fields
username_field = driver.find_element(By.ID,value="user-name")
password_field = driver.find_element(By.ID,value="password")
login_field = driver.find_element(By.ID,value="login-button")

#  Sending the keys 
username_field.send_keys(username)
password_field.send_keys(pasword)

# Checking the disable functionality disabled 

assert not login_field.get_attribute("disabled")

# Clicking the login button 
login_field.click()

# Make sure SECTORS HUB EXTENSION IS INSTALLED FROM YOUR BROWSER FOR YOUR LIFE TO BE EASY

# confirming that we have been logged in
success_element = driver.find_element(By.CSS_SELECTOR,value=".product_label")

assert success_element.text == "Products"# if they wont match it will rise an error
# But we logged in :) pew pew 

