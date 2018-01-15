# import libraries
from bs4 import BeautifulSoup
import requests

# specify the url
page = requests.get('http://tulsawebdesign.com/oscn/oscn.html')
soup = BeautifulSoup(page.text, 'html.parser')

case_list = soup.find(class_='caseCourtTable')
case_list_items = case_list.find_all('a')

# Use .contents to pull out the <a> tag's children
for case_list in case_list_items:
    names = case_list.contents[0]
    links = 'http://www.oscn.net/dockets/' + case_list.get('href')
    print(links)
    print(names)
