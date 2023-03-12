from bs4 import BeautifulSoup
import requests

URL = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table')
english_verb = table.find_all('td')[1::5]
russian_verb = table.find_all('td')[4::5]
diction_verb = {}
for i in range(len(english_verb)):
    diction_verb[english_verb[i].text.lstrip()] = russian_verb[i].text.lstrip()

if __name__ == '__main__':
    print(diction_verb)


