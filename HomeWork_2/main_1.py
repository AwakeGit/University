def middle_words(word):
    if len(word) % 2 == 0:
        return word[len(word) // 2 - 1:len(word) // 2 + 1]
    else:
        return word[len(word) // 2]


if __name__ == '__main__':
    txt = input('Введите слово: ')
    print(middle_words(txt))
