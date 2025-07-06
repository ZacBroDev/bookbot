
import sys

# pull book file and get text from book #
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_book():
    return get_book_text(sys.argv[1])

# pull: word count // character dictionary // list of dictionaries of each character #
from stats import get_num_words, total_characters, char_num_list

if len(sys.argv) == 2:
    # printing report # 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(get_num_words(print_book()))
    print("--------- Character Count -------")
    for item in char_num_list(total_characters(print_book())):
        char = item["char"]
        if char.isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# printing report # 
#print("============ BOOKBOT ============")
#print("Analyzing book found at books/frankenstein.txt...")
#print("----------- Word Count ----------")
#print(get_num_words(print_book()))
#print("--------- Character Count -------")
#1for item in char_num_list(total_characters(print_book())):
#    char = item["char"]
#    if char.isalpha():
#        print(f"{item["char"]}: {item["num"]}")
#print("============= END ===============")
