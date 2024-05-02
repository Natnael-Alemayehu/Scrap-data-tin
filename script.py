import requests
from bs4 import BeautifulSoup

def scrape_website(tin):
    url = f"https://example.com/{tin}"  # Replace "example.com" with the actual website URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Now you need to inspect the HTML structure of the website to identify the elements containing the information you need.
        # You can use the find() or find_all() methods of BeautifulSoup to extract data from specific HTML elements.

        # Example:
        # info_div = soup.find('div', class_='info')
        # info = info_div.text.strip()

        # Replace 'div' and 'class_' with the actual HTML tag and class of the element containing the information.

        # Once you've identified the elements, extract the data and return it.
        # You can return the data as a dictionary, list, or any other suitable data structure.

        # Example:
        # return {
        #     'info': info
        # }

        return soup  # For demonstration, returning the BeautifulSoup object

    else:
        print(f"Failed to retrieve data for TIN: {tin}. Status code:", response.status_code)
        return None

# List of TIN numbers
tin_numbers = ["1234567890", "9876543210", "5555555555"]  # Add your TIN numbers here

# Iterate through each TIN number and scrape the website
for tin_number in tin_numbers:
    data = scrape_website(tin_number)
    if data:
        print(f"Scraped data for TIN {tin_number}:", data)