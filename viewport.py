from selenium import webdriver
import time

# Since its a dedicated to viewports ,thats testing from different screen sizes
viewports = [(1024,768),(768,1024),(375,667),(414,896)]
driver = webdriver.Firefox()

url = "https://opensource-demo.orangehrmlive.com/"

url1 = "https://www.google.com/"
driver.get(url=url1)

# driver.set_window_size(width=768,height=1024)   #this is for one view port

try:
    for width,height in viewports:
        driver.set_window_size(width=width,height=height)
        time.sleep(2)
finally:
    driver.close()
