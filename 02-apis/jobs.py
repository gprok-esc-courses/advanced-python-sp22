import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.profesia.sk/en/work/?search_anywhere=python')
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')

# class="job-cardstyle__JobCardTitle-sc-1mbmxes-2 hwZGwa"

results = soup.find_all('span', class_='title')

for item in results:
    print(item.text)