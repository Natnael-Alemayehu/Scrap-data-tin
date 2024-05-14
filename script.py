from bs4 import BeautifulSoup
# from read_webpage import reading_webpage
from web_reader import page_reader

content = page_reader("0041038077")

soup = BeautifulSoup(content, 'lxml')

with open('content.txt', 'w') as file:
    file.write(content)


# Find the specific div tag
div_tags = soup.find_all('div', {'class': 'flex flex-col items-start'})
# print(type(div_tags))
for i,div_tag in enumerate(div_tags):
    if div_tag:
        span_tag = div_tag.find('span')
        if i == 0:
            registered_number = span_tag.text
            print(f"Registered number: {registered_number}")
        if i == 1:
            business_name = span_tag.text
            print(f"Business name: {business_name}")
    else:
        print("can't find span tag")