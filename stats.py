def count_words(text):
    word_lst = text.split()
    return len(word_lst)

def count_letters(text):
    letter_dic = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letter_dic:
            letter_dic[letter] = 1
        else:
            letter_dic[letter] += 1
    return letter_dic

def _sort_on(dic):
    return dic["count"]

def sort_letters(dic):
    sorted_lst = []
    for char, count in dic.items():
        _dic = {
            "char": char,
            "count":count
        }
        sorted_lst.append(_dic)
    sorted_lst.sort(reverse=True, key=_sort_on)
    return sorted_lst
