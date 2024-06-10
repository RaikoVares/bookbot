

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    character_count_dict = character_count(text)
    sorted_character_list = sort_character_dic(character_count_dict)
    print_report(num_words, sorted_character_list)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(text):
    text = text.lower()
    character_count_dict = {}
    for letter in text:
        if letter in character_count_dict.keys():
            character_count_dict[letter] += 1
        else:
            character_count_dict[letter] = 1
    return character_count_dict

def sorting_rule(dict):
    return dict["count"]

def sort_character_dic(character_count_dict):
    character_count_list = []
    for letter, count in character_count_dict.items():
        if letter.isalpha():
            _dic = {
                "letter": letter,
                "count": count
            }
            character_count_list.append(_dic)
    character_count_list.sort(reverse=True, key=sorting_rule)
    return character_count_list
        

def print_report(num_words, sorted_character_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_character_list:
        letter = item["letter"]
        count = item["count"]
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")



main()