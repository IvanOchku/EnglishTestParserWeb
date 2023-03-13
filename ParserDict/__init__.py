import requests
from bs4 import BeautifulSoup

from ParserDict import ParserNounOrAdjective
from ParserDict import ParserVerb


class Parser:
    def __init__(self, url: str):
        self.url = url
        self.dictionary = {}

    def get_table(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'lxml')
        table = soup.find('table')
        return table

    def get_dict(self) -> dict:
        table = self.get_table()
        english_verb = []
        russian_verb = []

        if 'glagolov' in self.url:
            english_verb = ParserVerb.get_english_verb(table)
            russian_verb = ParserVerb.get_russian_verb(table)

        if 'sushhestvitelnyh' in self.url or 'prilagatelnyh' in self.url:
            english_verb = ParserNounOrAdjective.get_english_noun_or_adjective(table)
            russian_verb = ParserNounOrAdjective.get_russian_noun_or_adjective(table)

        for i in range(len(english_verb)):
            self.dictionary[english_verb[i].text.lstrip()] = russian_verb[i].text.lstrip()

        return self.dictionary


if __name__ == '__main__':
    URL_VERB = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'
    URL_NOUN = 'https://elenaruvel.com/150-populyarnyh-anglijskih-sushhestvitelnyh-s-ozvuchkoj/'
    URL_ADJECTIVE = 'https://elenaruvel.com/150-bazovyh-anglijskih-prilagatelnyh-s-ozvuchkoj/'

    print(Parser(URL_VERB).get_dict())
    print(Parser(URL_NOUN).get_dict())
    print(Parser(URL_ADJECTIVE).get_dict())
