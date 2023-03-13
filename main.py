from random import randint

import ParserDict
import BrokenDict

URL_VERB = 'https://elenaruvel.com/150-vazhnyh-anglijskih-glagolov-s-ozvuchkoj/'
URL_NOUN = 'https://elenaruvel.com/150-populyarnyh-anglijskih-sushhestvitelnyh-s-ozvuchkoj/'
URL_ADJECTIVE = 'https://elenaruvel.com/150-bazovyh-anglijskih-prilagatelnyh-s-ozvuchkoj/'


class EnglishTest:
    count_correct_answers = 0
    count_amount_words = 0

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.dictionary_copy = self.dictionary.copy()
        self.amount_words = len(self.dictionary_copy)

    def get_key_by_random_index(self):
        try:
            index = randint(0, len(self.dictionary_copy) - 1)
            keys_lst = list(self.dictionary_copy.keys())
            return keys_lst[index]
        except ValueError:
            return

    def check_answer(self, key: str, ans: str):
        correct_answers = self.dictionary_copy[key]
        if ans == correct_answers or set(ans.split(', ')).issubset(set(correct_answers.split(', '))):
            return True
        return False

    def remove_key(self, key):
        self.dictionary_copy.pop(key)

    def get_assessment(self):
        assessment = self.count_correct_answers / self.amount_words
        if 0.9 <= assessment <= 1:
            return f'You are amazing! Amount of correct answers: {self.count_correct_answers}'
        elif 0.7 <= assessment < 0.9:
            return f'Not bad but you can better! Amount of correct answers: {self.count_correct_answers}'
        elif 0.5 <= assessment < 0.7:
            return f'Learn harder! Amount of correct answers: {self.count_correct_answers}'
        else:
            return f'This is so bad. Amount of correct answers: {self.count_correct_answers}'

    def reboot(self):
        self.dictionary_copy = self.dictionary.copy()
        self.amount_words = len(self.dictionary_copy)
        self.count_amount_words = 0
        self.count_correct_answers = 0
        self.test_start()

    def test_start(self):
        while True:
            try:
                area_words = input(f'Choose number words from 0 to {self.amount_words} through the colon without spaces. Example: "0:20": ')
                start_index, end_index = area_words.split(':')
                if not start_index.isdigit() or not end_index.isdigit() or int(end_index) > self.amount_words:
                    continue
                self.dictionary_copy = BrokenDict.broken_dict(int(start_index), int(end_index), self.dictionary)
                self.amount_words = int(end_index) - 1
            except ValueError:
                continue
            else:
                break

        while True:
            key = self.get_key_by_random_index()
            if key is None or self.count_amount_words == self.amount_words:
                print(self.get_assessment(), 'Would you like another?', end='\n')
                again = input().lower()
                if again == 'no':
                    break
                else:
                    self.reboot()

            ans = input(f'{key}: ').lower()

            if self.check_answer(key, ans):
                self.count_correct_answers += 1
                print(f'Well done! All answer options: {self.dictionary_copy[key].upper()}')
            else:
                print(f'You are wrong :( The right answer is: {self.dictionary_copy[key].upper()}')

            self.count_amount_words += 1
            self.remove_key(key)


EnglishTest(ParserDict.Parser(URL_NOUN).get_dict()).test_start()
