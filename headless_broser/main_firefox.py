import time
import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_driver():
    """Try to get a webdriver instance, with multiple fallbacks"""
    drivers = [
        (try_chrome, "Chrome"),
        (try_firefox, "Firefox"),
        (try_requests_only, "Requests (fallback)")
    ]
    
    for driver_func, name in drivers:
        try:
            logger.info(f"Attempting to use {name}...")
            driver = driver_func()
            logger.info(f"Successfully initialized {name}")
            return driver
        except Exception as e:
            logger.error(f"{name} initialization failed: {str(e)}")
    
    raise RuntimeError("All browser options failed. Unable to proceed with scraping.")

def try_chrome():
    """Try to initialize Chrome WebDriver"""
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")  # Updated headless argument
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        logger.warning(f"ChromeDriver installation failed: {e}")
        # Try with executable_path if ChromeDriverManager fails
        try:
            service = ChromeService(executable_path="/usr/bin/chromedriver")
            return webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e2:
            logger.warning(f"ChromeDriver with direct path failed: {e2}")
            raise

def try_firefox():
    """Try to initialize Firefox WebDriver"""
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("-headless")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.set_preference("general.useragent.override", 
                                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0")
    
    try:
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=firefox_options)
    except Exception as e:
        logger.warning(f"GeckoDriver installation failed: {e}")
        # Try with executable_path if GeckoDriverManager fails
        try:
            service = FirefoxService(executable_path="/usr/bin/geckodriver")
            return webdriver.Firefox(service=service, options=firefox_options)
        except Exception as e2:
            logger.warning(f"GeckoDriver with direct path failed: {e2}")
            raise

class RequestsFallback:
    """A minimal fallback that mimics a subset of the WebDriver API using requests"""
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.page_source = None
        
    def get(self, url):
        """Get the webpage content"""
        response = self.session.get(url)
        response.raise_for_status()
        self.page_source = response.text
        return response
        
    def quit(self):
        """Close the session"""
        self.session.close()

def try_requests_only():
    """Create a fallback using just requests"""
    return RequestsFallback()

def scrape_neuralnine_books():
    """Scrape the books from neuralnine.com"""
    driver = None
    
    try:
        driver = get_driver()
        url = "https://www.neuralnine.com/books"
        
        if isinstance(driver, RequestsFallback):
            logger.info("Using requests fallback mode")
            driver.get(url)
        else:
            logger.info(f"Using Selenium with {driver.name}")
            driver.get(url)
            # Wait for page to load
            time.sleep(3)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Try different selectors if the first one fails
        headings = soup.find_all("h2", class_="elementor-heading-title")
        if not headings:
            logger.info("No h2 headings found with class 'elementor-heading-title', trying alternative selectors")
            headings = soup.find_all("h2")
            
        if not headings:
            logger.info("Still no headings found, trying to find book titles by other means")
            # Look for elements that might contain book information
            headings = soup.find_all(class_=lambda c: c and ('book' in c.lower() or 'title' in c.lower()))
            
        if not headings:
            logger.warning("No book information found on the page")
            print("No book information could be found.")
        else:
            print("\nBooks listed on NeuralNine:\n")
            for i, heading in enumerate(headings, 1):
                print(f"{i}. {heading.getText(strip=True)}")
                
    except Exception as e:
        logger.error(f"Scraping failed: {str(e)}")
        print(f"Error occurred during scraping: {str(e)}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    scrape_neuralnine_books()