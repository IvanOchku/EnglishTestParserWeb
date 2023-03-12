import ParserDict

URL_VERB = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'
URL_NOUN = 'https://elenaruvel.com/150-populyarnyh-anglijskih-sushhestvitelnyh-s-ozvuchkoj/'

print(ParserDict.Parser(URL_NOUN).get_dict())
print(ParserDict.Parser(URL_VERB).get_dict())
