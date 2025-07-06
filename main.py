def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def print_book():
    return get_book_text("books/frankenstein.txt")

from stats import get_num_words, total_characters, char_num_list


print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(get_num_words(print_book()))
print("--------- Character Count -------")
for item in char_num_list(total_characters(print_book())):
    char = item["char"]
    if char.isalpha():
        print(item["char"],": ", item["num"])
print("============= END ===============")

