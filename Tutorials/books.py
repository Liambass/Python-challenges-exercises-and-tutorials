# Create a dictionary where they keys are books, and the values are their authors.

# >>> books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
# We can query the author of any book.

# >>> print(books["The Handmaiden's Tale"])
# 'Margaret Atwood'
# However if we try to query what books have been written by an author, we get the following error.

# >>> print(books["Margaret Atwood"])
# KeyError: 'Margaret Atwood'
# This is because "Margaret Atwood" is a value not a key.
# Recall we cannot query a dictionary using a value.


books = {"The Handmaiden's Tale":"Margaret Atwood", 
    "The Hobbit":"J.R.R. Tolkien", 
    "Charlie and the Chocolate Factory":"Roald Dahl"}


authors = {"Margaret Atwood":["The Handmaiden's Tale"], 
    "J.R.R. Tolkien":["The Hobbit", "The Lord of the Rings"], 
    "Roald Dahl":["Charlie and the Chocolate Factory", "George's Marvellous Medicine"]}

print(authors["Roald Dahl"])

