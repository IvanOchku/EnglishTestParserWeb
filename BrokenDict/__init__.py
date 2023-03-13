def broken_dict(start_index: int, end_index: int, dictionary: dict) -> dict:
    items = list(dictionary.keys())
    broken_dictionary = {}
    for i in range(start_index, end_index):
        try:
            broken_dictionary[items[i]] = dictionary[items[i]]
        except IndexError:
            break
    return broken_dictionary


if __name__ == '__main__':
    print(broken_dict(0, 1, {'hi': 'привет, здравствуйте'}))

