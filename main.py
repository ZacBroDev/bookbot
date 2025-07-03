def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def print_book():
    return get_book_text("books/frankenstein.txt")

    
def get_num_words():
   num_words = 0
   words = print_book().split()

   for word in words:
       num_words += 1
   message = f"{num_words} words found in the document"
   return message

print(get_num_words())
