def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def print_book():
    return get_book_text("books/frankenstein.txt")

from stats import get_num_words

print(get_num_words(print_book()))
