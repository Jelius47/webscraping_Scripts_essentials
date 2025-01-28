# Broken images on a website are images that do not display properly,
#  often showing up as a placeholder icon or a blank space

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

url ="https://the-internet.herokuapp.com/broken_images"

driver = webdriver.Firefox()

driver.get(url=url)

# Capturing my images 
images = driver.find_elements(By.TAG_NAME,value="img") #All tags with img represents images 

# Capturing broken images 
broken_images = []

for image in images:
    src = image.get_attribute("src")
    if src :
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found")

if broken_images:
    for br_image in broken_images:
        print(br_image)        
    else:
        print("No Broken Image: ")


driver.quit()
