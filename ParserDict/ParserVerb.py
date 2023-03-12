def get_russian_verb(table):
    russian_verb = table.find_all('td')[4::5]
    return russian_verb


def get_english_verb(table):
    english_verb = table.find_all('td')[1::5]
    return english_verb
