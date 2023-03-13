import ParserDict

URL_VERB = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'
URL_NOUN = 'https://elenaruvel.com/150-populyarnyh-anglijskih-sushhestvitelnyh-s-ozvuchkoj/'
URL_ADJECTIVE = 'https://elenaruvel.com/150-bazovyh-anglijskih-prilagatelnyh-s-ozvuchkoj/'

print(ParserDict.Parser(URL_NOUN).get_dict())
print(ParserDict.Parser(URL_VERB).get_dict())
print(ParserDict.Parser(URL_ADJECTIVE).get_dict())
