# Example you are browsing using selenium driver then the pop up
# message says "jelius.com says Are you good !!"
# Then from there we can not proceed because of the alert
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/javascript_alerts"

browser.get(url=url)

Allert_button = browser.find_element(By.XPATH,value="//button[normalize-space()='Click for JS Confirm']")

Allert_button.click() # This wont click at all

# We have to switch to the alert
alert = browser.switch_to.alert
alert_text = alert.text # This could be fed into ai for either to confirm or not 
print(alert_text)

# How can I click it 
# alert.accept()
alert.dismiss() # To dismiss it 
# alert.send_keys("fdkm") # to send keys to the alert
