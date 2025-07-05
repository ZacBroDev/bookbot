def get_num_words(book):
   num_words = 0
   words = book.split()

   for word in words:
       num_words += 1
   message = f"{num_words} words found in the document"
   return message

def total_characters(book):
    char_directory = {}
    char_list = list(book.lower())

    for char in char_list:
        if char not in char_directory:
            char_directory[char] = 0
        if char in char_directory:
            char_directory[char] = (char_directory[char] + 1)

    return print(char_directory)
