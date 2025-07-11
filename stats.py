# count total number of words in book and print message #
def get_num_words(book):
   num_words = 0
   words = book.split()

   for word in words:
       num_words += 1
   message = f"Found {num_words} total words"
   return message

# counting the amount each character appears in book #
def total_characters(book):
    char_directory = {}
    char_list = list(book.lower())

    for char in char_list:
        if char not in char_directory:
            char_directory[char] = 0
        if char in char_directory:
            char_directory[char] = (char_directory[char] + 1)

    return char_directory

# create key for sorting in def charm_num_list(book) #
def sort_on(items):
    return items["num"]

# create list of dictionaries to sort characters and count #
def char_num_list(book):
    new_list = []
    for char,num in book.items():
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = num
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list


