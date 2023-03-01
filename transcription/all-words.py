from bs4 import BeautifulSoup
import requests
from mediapp import get_coordinator
import datetime

words_data = []

# get coordinates for all words
start = datetime.datetime.now()
data = requests.post('https://www.handspeak.com/word/index-searchdictV2.php', {'page': 1,
    'query': None,
    'filter': 'all',})
soup = BeautifulSoup(data.text, features="html.parser")

item = max([int(i.get('data-page_number')) for i in soup.find_all('a', {'class':'page-link'}) if i.get('data-page_number') is not None])

for i in range(1, item+1):
    data = requests.post('https://www.handspeak.com/word/index-searchdictV2.php', {'page': i,
        'query': None,
        'filter': 'all',})
    soup = BeautifulSoup(data.text, features="html.parser")
    for item in soup.find_all('a', title=True):
        data = requests.get(f"https://www.handspeak.com{item.get('href')}")
        soup = BeautifulSoup(data.text, features="html.parser")
        if soup.find('video') and soup.find('video')['src']:
            words_data.append({'url': soup.find('video')['src'], 'title': item.text})

end = datetime.datetime.now()
print('--------------difference--------------', start, end, end - start)
print("---------------->words_data:-", words_data)

for word in words_data:
    get_coordinator(word)