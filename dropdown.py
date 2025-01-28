import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # This is to be able to work with drop downs
url ="https://the-internet.herokuapp.com/dropdown"

driver = webdriver.Firefox()

driver.get(url=url)
# Finding the dropdown element

dropdown_element = driver.find_element(By.ID,value="dropdown")

selected_element = Select(dropdown_element)
# 1.Selecting a value by visible text 
selected_element.select_by_visible_text("Option 2")
time.sleep(3)
# 2.Selecting a value by Index
selected_element.select_by_index(1)# Indexing count starts from 0 : the index for option 1 is 1
time.sleep(3)
# 3.Selecting a value by using a value 
selected_element.select_by_value("2") # This is the value for option 2
time.sleep(3)

# trying to count the dropdowns i have 
option_count = len(selected_element.options) # This will include the whole array of values indexes


# using the click method 
targeted_elemnt = "Option 2"

for option in selected_element.options:
    if option.text == targeted_elemnt:
        option.click()
        print(f"Selected option is: {targeted_elemnt}")
        break
    else:
        print(f"Option {targeted_elemnt} not found !!")

expected_counts = 3

if option_count ==expected_counts:
    print("Succesfully passed the test ")
else:
    print("There is an issue: !!")

driver.close()

