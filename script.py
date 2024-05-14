from bs4 import BeautifulSoup
# from read_webpage import reading_webpage
from web_reader import page_reader

content = page_reader("0041038077")

soup = BeautifulSoup(content, 'lxml')

with open('content.txt', 'w') as file:
    file.write(content)


# Business name and registered number is captured
def business_name_registered_number():
    """
    This function returns business name and registered number
    
    return business_name , registered_number
    """
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
    return business_name , registered_number

# Not sure yet
def other_info():
    div_tags = soup.find_all('div', {'class': 'flex flex-col items-start justify-between'})
    # print(type(div_tags))
    for i,div_tag in enumerate(div_tags):
        if div_tag:
            span_tag = div_tag.find('span')
            if i == 0:
                tin_number = span_tag.text
                # print(f"Tin number: {tin_number}")
                
            if i == 1:
                business_name_amharic = span_tag.text
                # print(f"Business name amharic: {business_name_amharic}")
            if i == 2:
                legal_condition_amharic = span_tag.text
                # print(f"Legal Condition Amharic: {legal_condition_amharic}")
            if i == 3:
                capital = span_tag.text
                # print(f"capital: {capital}")
            if i == 4:
                registered_date = span_tag.text # I am not sure what data this is. 
                # print(f"Date NOT SURE: {date_not_sure}")
        else:
            print("can't find span tag")
    return tin_number, business_name_amharic, legal_condition_amharic, capital, registered_date

    return tin_number, business_name_amharic, legal_condition_amharic,capital,date_not_sure
def person_position_name_and_image():
    div_tags = soup.find('div', {'class': 'flex flex-col items-center ng-star-inserted'})
    # print(type(div_tags))
    if div_tags:
        image_link = div_tags.find(class_="sepia-0 w-28 h-28 bg-gray-300 rounded-md shadow mb-4 shrink-0 p-1").get('src')
        person_name_amharic = div_tags.find('h1').text
        person_name_english = div_tags.find('p').text
        print(image_link)
        print(person_name_amharic)
        print(person_name_english)
    else:
        print("can't find span tag")
    person_position = soup.find('p', class_="text-md text-gray-700 uppercase font-bold tracking-wider mb-2").text
    print(person_position)
print(other_info())