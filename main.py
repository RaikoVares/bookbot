from stats import count_words
from stats import count_letters
from stats import sort_letters

def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")


    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")


    print("----------- Character Count ----------")
    for data_pair in sorted_characters:
        if data_pair["char"].isalpha():
            print(f"{data_pair['char']}: {data_pair['count']}")

    print("============= END ===============")

def main():
    path = "books/frankenstein.txt"
    text = get_books_text(path)
    word_count = count_words(text) 
    letter_count_dic = count_letters(text)
    sorted_characters = sort_letters(letter_count_dic)
    print_report(path, word_count, sorted_characters)

main()
