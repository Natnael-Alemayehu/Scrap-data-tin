from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def page_reader(tin=""):
    # Path to your ChromeDriver executable
    chrome_driver_path = 'chromedriver'

    # URL of the website you want to scrape
    url = f'https://etrade.gov.et/business-license-checker?tin={tin}'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode, i.e., without a GUI
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage')  # Disable /dev/shm usage

    # Set up ChromeDriver service
    service = Service(chrome_driver_path)

    # Initialize Chrome webdriver with configured options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Load the webpage
        driver.get(url)

        # Wait for the page to fully render (you may need to adjust the timeout value)
        driver.implicitly_wait(10)

        # Extract the page content after rendering
        page_content = driver.page_source

        # Print or process the page content as needed
        return(page_content)
        
        with open('content.txt', 'w') as file:
            file.write(page_content)

    finally:
        # Quit the webdriver
        driver.quit()