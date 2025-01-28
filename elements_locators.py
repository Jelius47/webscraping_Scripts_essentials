#  locators are used to identify and interact with 
# specific elements on a web page.
# source:
# https://search.brave.com/search?q=locaters+and+elments+in+html&source=web&summary=1&conversation=ac6670389f0cbbcda068d7

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setting up some configurations

driver = webdriver.Firefox()
driver.get("https://selenium.dev/")

tittle = driver.title

assert "Selenium" in tittle # Configuring/checking  the title of the site we are scrapping

driver.find_element(By.XPATH("RNNXgb"))# Make sure the id exists in your website

# When you are unable to find the elements by their html elements then its better to find them 
# using css and xpath

# CSS selectors are simpler and faster, 
# making them ideal for straightforward HTML element selection. 
# They are more readable and easier to learn compared to XPath. 
# CSS selectors are compatible with all modern browsers and can be created 
# using driver developer tools.

# XPath, on the other hand, offers more flexibility and power, 
# capable of navigating complex and dynamic web page structures, 
# including non-HTML elements. XPath allows bidirectional flow, 
# enabling traversal from parent to child and child to parent, 
# which is not possible with CSS selectors.

# Xpath are basically xml structure


# Key takeouts 
# Elements
# -checkbox -Links and Text fields

# Locators
# -ID ,Name ,class name
# -CSS selectors,XPath,Link Text
# -Partial link text,TagName

# Interactions
# -TextField: Typing things
# -Checkboxes: checking the boxes
# -Link: Clicking on a link  

# Assertions 
# Verifying the functionality 
# --Eg: Verifying that there should be a button with text "submit"


