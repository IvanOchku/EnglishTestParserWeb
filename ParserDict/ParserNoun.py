def get_russian_noun(table):
    russian_verb = table.find_all('td')[3::4]
    return russian_verb


def get_english_noun(table):
    english_verb = table.find_all('td')[2::4]
    return english_verb
