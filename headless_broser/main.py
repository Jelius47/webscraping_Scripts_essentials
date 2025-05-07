# import time

# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options


# # The headless stuffs
# # Configure Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")                # Disable sandboxing for compatibility (e.g. in Docker)
# chrome_options.add_argument("--headless")                  # Run Chrome in headless mode (no GUI)
# chrome_options.add_argument("--disable-dev-shm-usage")     # Avoid issues with limited shared memory

# # Create a Service object using ChromeDriverManager
# service = Service(ChromeDriverManager().install())

# # Initialize the WebDriver using the Service and Options
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # url configuration
# url = "https://www.neuralnine.com/books"

# driver.get(url=url)

# soup = BeautifulSoup(driver.page_source, features="lxml")

# headings = soup.find_all(name="h2",attrs={"class":"elementor-heading-title"})
# for heading in headings:
#     print(heading.getText())

# time.sleep(3)
# driver.quit()

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver():
    # Try Chrome first
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_service = ChromeService(ChromeDriverManager().install())

        print("Launching Chrome browser...")
        return webdriver.Chrome(service=chrome_service, options=chrome_options)

    except Exception as chrome_error:
        print(f"[!] Chrome failed: {chrome_error}")
        print("=> Falling back to Firefox...")

        # Try Firefox next
        try:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("-headless")
            firefox_service = FirefoxService(GeckoDriverManager().install())

            print("Launching Firefox browser...")
            return webdriver.Firefox(service=firefox_service, options=firefox_options)

        except Exception as firefox_error:
            print(f"[!] Firefox also failed: {firefox_error}")
            raise RuntimeError("Both Chrome and Firefox failed to launch.")


def scrape_neuralnine_books():
    driver = get_driver()
    try:
        url = "https://www.neuralnine.com/books"
        driver.get(url)

        # Wait for the page to fully load (optional delay)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "lxml")

        headings = soup.find_all("h2", class_="elementor-heading-title")
        if not headings:
            print("No headings found.")
        else:
            print("\nBooks listed on NeuralNine:\n")
            for heading in headings:
                print("•", heading.getText(strip=True))

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_neuralnine_books()
