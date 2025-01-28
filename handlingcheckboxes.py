from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://designsystem.digital.gov/components/checkbox/"

browser = webdriver.Firefox()

browser.get(url=url)

# Excecuting javascript
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
browser.find_element(By.XPATH,"//label[@for='check-historical-douglass-2']").click()

# Now i want to check all of the checkboxes 
# Understand Checkbox HTML Structure:
# Checkbox elements usually follow this basic pattern:

# html code : <input type="checkbox" id="check-historical-douglass-2" name="example">

# Use XPath to Select by Attribute:
# XPath allows querying by specific attributes. The expression //input[@type='checkbox'] does the following:

# //: Selects elements anywhere on the page.
# input: Targets all <input> elements.
# [@type='checkbox']: Filters for elements where the type attribute is "checkbox".

checkboxes = browser.find_elements(By.XPATH,"//input[@type='checkbox']")

# Click each checkbox
# for checkbox in checkboxes:
#     # Check if it's not already selected
#     if not checkbox.is_selected():
#         checkbox.click()
for checkbox in checkboxes:
   try:
     if not checkbox.send_keys(Keys.SPACE):
      browser.execute_script("arguments[0].click();", checkbox)
   finally:
     # closing my browser
    time.sleep(4)
    browser.close()
     
