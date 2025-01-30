# An iframe, or inline frame, in HTML is an element 
# represented by the <iframe> tag. It allows you to embed another 
# webpage or document within the current webpage. 
# This element functions as a ‘window’ on your webpage through which 
# visitors can view and interact with content from a different source.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

url ="https://the-internet.herokuapp.com/iframe"

browser.get(url=url)

# First we identify the iframe 
iframe = browser.find_element(By.ID,value="mce_0_ifr")

# Switching to the frame 
browser.switch_to.frame(iframe)

# Finding the desired element within the current frame 
Text_editor = browser.find_element(By.ID,value="tinymce")

# Since this element is a text editor and can be use to write things 

Text_editor.clear() # Clearing the text if there is an input arledy 

Text_editor.send_keys("Glory t GOD I am succesfully practising web scrapping : :)")

time.sleep(3)
# switching to the default frame of our page 

browser.switch_to.default_content() # Switches the focus to the default frame

selenium_link = browser.find_element(By.XPATH,value="//:a[normalize-space()='Elemental Selenium]")
selenium_link.click()
