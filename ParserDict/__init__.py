import requests
from bs4 import BeautifulSoup

import ParcerNoun
import ParserVerb

URL_VERB = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'
URL_NOUN = 'https://elenaruvel.com/150-populyarnyh-anglijskih-sushhestvitelnyh-s-ozvuchkoj/'


class Parser:
    def __init__(self, url):
        self.url = url
        self.dictionary = {}

    def get_table(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'lxml')
        table = soup.find('table')
        return table

    def get_dict(self):
        table = self.get_table()

        if 'glagolov' in self.url:
            english_verb = ParserVerb.get_english_verb(table)
            russian_verb = ParserVerb.get_russian_verb(table)

        for i in range(len(english_verb)):
            self.dictionary[english_verb[i].text.lstrip()] = russian_verb[i].text.lstrip()

        return self.dictionary


print(Parser(URL_NOUN).get_dict())

