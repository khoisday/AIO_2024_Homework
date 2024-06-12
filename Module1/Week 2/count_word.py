def count_words(file_path: str):
    with open(file_path, 'r') as f:
        lines = f.read()

    words = lines.split()
    word_dict = dict()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


if __name__ == "__main__":
    file = "P1_data.txt"
    print(count_words(file))
