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
