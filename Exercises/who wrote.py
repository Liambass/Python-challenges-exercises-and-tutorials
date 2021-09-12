# given the following dictionary of authors and books:
# books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}
# write a function which:
# - Takes a book title as an argument
# - for each author, searches through the list of associated book titles in the dictionary and if the given title is in the list, returns "{author} wrote {title}", where author and title should be the names of the author and the book respectively. If the book is not in any of the lists, simply return "Book not found"
# - the case the user enters the title in should not matter (hint: the books are all listed in title case, so find out how to convert a string to title case)
# incorporate this function into a program which asks the user to input a book title, and prints the result of calling this function on the given title

import string

def whowrote(book):
    for author in books:
        if book in books[author]:
            return f"{author} wrote {book}"
    return f"\"{book}\" not found"

books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}

while True:
    book = string.capwords(input("book? "))
    print(whowrote(book))
    cont = input("Another? (Y/N) ").upper()
    if cont[0] == "Y":
        continue
    else:
        exit()