import csv
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://cosmocode.io/automation-practice-webtable"

browser= webdriver.Firefox()
browser.get(url=url)

# For this kind of website the table is not visisble unles you scroll
browser.execute_script("window.scrollTo(0,700)")

table = browser.find_element(By.ID,value="countries")

rows = table.find_elements(By.TAG_NAME, "tr")
data = []

# Iterate through rows and extract data
for row in rows:
    # Find all header or data cells
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    if row_data:  # Avoid empty rows
        data.append(row_data)

# Save table data to CSV
# Checking the existence of the file path
csv_file_path = "table_data.csv"
os.path.exists(csv_file_path)

if csv_file_path == "table_data.csv":
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data successfully saved to {csv_file_path}")
else:
    print("Skipping file creation as the filename is not 'table_data.csv'")


# # Using pandas approach
# # Though it has few issues with it heading

# #  Extract table headers
# headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]

# # Extract table rows
# rows = table.find_elements(By.TAG_NAME, "tr")
# data = []

# for row in rows[1:]:  # Skip the header row
#     cells =  row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
#     row_data = [cell.text for cell in cells]
#     if row_data:  # Avoid empty rows
#         data.append(row_data)

# # Create a DataFrame
# df = pd.DataFrame(data, columns=headers)

# # Save DataFrame to CSV
# csv_file_path2 = "table_data_pandas.csv"
# df.to_csv(csv_file_path, index=False, encoding="utf-8")
# print(f"Data saved to {csv_file_path2}")

browser.quit()