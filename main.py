

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    character_count_dict = character_count(text)
    print(num_words)

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
    print(character_count_dict)
        

main()