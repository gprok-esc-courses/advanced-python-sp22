import requests
from xml.etree.ElementTree import fromstring

feed = requests.get('https://www.yahoo.com/news/rss/world')
content = feed.content
root = fromstring(content)

for news in root.iter('item'):
    title = news.find('title')
    print(title.text)