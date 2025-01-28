# Broken links -- Are links that no longer work, often leading to a
#  404 page error or similar message indicating the webpage is
#  not available.
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests # type: ignore 
# type: igore will ignore any error of the imported library



driver = webdriver.Firefox()
url = "https://jqueryui.com/"

driver.get(url=url)

# capturing all links 
all_links = driver.find_elements(By.TAG_NAME,value="a") # Meaning all anchour tags 
print(f"Total number of links of the page {len(all_links)}")
broken_links = []
for link in all_links:
    href = link.get_attribute("href")
    response = requests.get(href)
    print(response ,"\n")

    if response.status_code >= 400:
        print(f"Broken link: {href} Status code: {response.status_code}")
        broken_links.append(href)
# Printing  all broken links 
print("_________::::: BROKEN LINKS :::::_______")
for link in broken_links:
    print(link)

driver.quit()
