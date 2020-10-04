from itertools import product


def max_in_dict(dict_):
    max_ = -1
    max_key = ' '
    for key in dict_:
        if dict_[key] > max_:
            max_ = dict_[key]
            max_key = key
    return max_key


def standard_library_task2():
    """
    2. Написать функцию, которая для полученного текста возвращает
     самое популярное слово,
    самую популярную букву и среднее количество вхождений буквы в слово.
    """
    s = str(input())
    words = {}
    letters = {}
    fst_letter = -1
    c = s[0]
    if not c.isalpha():
        in_word = False
    else:
        in_word = True
        fst_letter = 0
    for i in range(1, len(s)):
        letter = s[i]
        if in_word:
            if not letter.isalpha():
                in_word = False
                word = s[fst_letter:i]
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
            else:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
        else:
            if not letter.isalpha():
                continue
            else:
                in_word = True
                fst_letter = i
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1

    number_of_words = len(words)
    print("The most frequent word:", max_in_dict(words))
    print("The most frequent letter:", max_in_dict(letters))
    for letter in letters:
        print(letter + ":", letters[letter] / number_of_words)


def standard_library_task3():
    """
    3. Написать функцию, которая принимает на вход алфавит
     и выдаёт все палиндромы этого алфавита не больше указанной длины.
    """
    len_of_palindrome = int(input())
    alphabet = [str(i) for i in input().split()]
    if len_of_palindrome % 2 == 0:
        n = len_of_palindrome // 2
        for i in product("".join(alphabet), repeat=n):
            print(*i, end=" ")
            print(*i[::-1], end="\n")
    else:
        n = (len_of_palindrome + 1) // 2
        for i in product("".join(alphabet), repeat=n):
            print(*i, end=" ")
            print(*i[1::-1], end="\n")




