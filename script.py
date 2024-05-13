from bs4 import BeautifulSoup
from read_webpage import reading_webpage

content = reading_webpage("0041038077")

soup = BeautifulSoup(content, 'lxml')

# Find the specific div tag
div_tag = soup.find('div', {'class': 'flex flex-col items-start'})

# Check if the div tag was found
if div_tag:
    # Extract the text from the span tag inside the div
    span_tag = div_tag.find('span')
    if span_tag:
        business_name = span_tag.text.strip()
        print(business_name)
    else:
        print("Could not find the span tag inside the div.")
else:
    print("Could not find the div tag with the specified class name.")
