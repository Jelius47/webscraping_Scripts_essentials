from selenium import webdriver
from selenium.webdriver.common.by import By

url ="https://the-internet.herokuapp.com/nested_frames"

# creating a drive
driver = webdriver.Firefox()

driver.get(url=url)

# switch to top frame
driver.switch_to.frame("frame-top")
# Now we are inside the frame 


# Switch to the middle frame 
driver.switch_to.frame("frame-middle")

# Locating the content within middle frame
content = driver.find_element(By.ID,value="content").text
print(f"The content of the middle frame {content}")

# Switching to bottom 


# First switch to default content
driver.switch_to.default_content()

# switching to bottom content
driver.switch_to.frame("frame-bottom")
content_bottom = driver.find_element(By.TAG_NAME,value="body").text
print(f"Content of the bottom: {content_bottom}")