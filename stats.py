def get_num_words(book):
   num_words = 0
   words = book.split()

   for word in words:
       num_words += 1
   message = f"{num_words} words found in the document"
   return message