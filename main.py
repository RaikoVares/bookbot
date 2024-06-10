

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(num_words)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def get_num_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count
    

main()