
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime,timedelta

url = "https://www.globalsqa.com/demo-site/datepicker/"

browser = webdriver.Firefox()
browser.get(url=url)

# Inspecting the html structure you might find the date picker inside the frame 

# Before switching we click the small alert about date pickinig
browser.find_element(By.XPATH,value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()


# Swithing inside the frame 
frame_date = browser.find_element(By.XPATH,value="//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame_date)

time.sleep(3)
# Selecting the date picker 
date_picker = browser.find_element(By.CSS_SELECTOR,value="#datepicker")
date_picker.click()


# If you are required to fill in the current date time 
current_date = datetime.now()

next_day = current_date + timedelta(days=1)
yesterday = current_date + timedelta(days=-1)

# the date must comply with specifications of the callender 

formated_date = yesterday.strftime("%m/%d/%y")

# send the keys or you date 
date_picker.send_keys(formated_date +Keys.TAB) # So as to mimic the date picker its like hitting enter 
# for any kind of picker atleast it will work unless its a dropdown one 

# Dealing with dropdown date pickers 
url2 = "https://demo.automationtesting.in/Datepicker.html"

browser.switch_to.new_window() #Switching to new window

browser.get(url=url2)

current_month  = datetime.now().month
current_year = current_date.year #Still it will work



# locate the date filling box
date_box = browser.find_element(By.ID,value="datepicker2").click()

time.sleep(3)
current_date # Remember we created this earlier

next_date_day = str(current_date + timedelta(days=1)).day

current_month = str(datetime.now().month)

current_year_ = str(current_date.year)

next_month = (current_month % 12) + 1 # AAAh this is a genius trick 

# SINCE BASED ON THE DROPDOWN THE VALUE ARE MOTH/YEAR IN THE HTML STRUCTURE

next_month_year = f"{next_month}/{current_year_}"

# Finding the dropdown 

month_dropdown = browser.find_element(By.CSS_SELECTOR,value="select[title='change the month']")

select = Select(month_dropdown)

select.select_by_value(str(next_month_year))

# Finding years dropdown
years_dropdown = browser.find_element(By.CSS_SELECTOR,value="select[title='change the year']")
select = Select(years_dropdown)
select.select_by_visible_text("2002")

browser.find_element(By.LINK_TEXT,next_day).click()