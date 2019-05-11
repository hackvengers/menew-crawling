from bs4 import BeautifulSoup
import requests




words = ['된장찌개']

url_wiki_home = 'https://en.wikipedia.org/wiki/'

url_wiki = url_wiki_home+words[0]
req_wiki = requests.get(url_wiki)
html_wiki = req_wiki.text
print(html_wiki)