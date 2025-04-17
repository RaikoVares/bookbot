

def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_books_text(path)
    print(text)

main()
