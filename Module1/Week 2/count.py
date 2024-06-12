def count_char(word: str):
    char_dict = dict()

    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict
