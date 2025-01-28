from selenium import webdriver
from selenium.webdriver.common.by import By 
url1 = "https://www.selenium.dev/"
url2 = "https://www.playwright.dev"

browser = webdriver.Firefox()
browser.get(url=url1)

browser.switch_to.new_window()# This will just open a new window and completely moven with script
browser.get(url=url2) # Provided this will result the new tab to be playwright

# Checking the number of tabs opened
number_of_tabs =  len(browser.window_handles)
print(number_of_tabs)

# Also printing tabs values
tabs_values = browser.window_handles
print(tabs_values)
# also for current window 
Current_tab = browser.current_window_handle
print(Current_tab)

browser.find_element(By.CSS_SELECTOR,value=".getStarted_Sjon").click()

# Locating my first tab
FirstTab = browser.window_handles[0]

if Current_tab != FirstTab:
    browser.switch_to.window(FirstTab)
# We are sure that we are on First Tab
browser.find_element(By.XPATH,value="//span[normalize-space()='Downloads']").click()
