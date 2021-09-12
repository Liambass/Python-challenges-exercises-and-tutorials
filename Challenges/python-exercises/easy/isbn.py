
def checksum(isbn):
    check = 0
    i = 0
    while i < 12:
        if i % 2 == 0:
            check += int(isbn[i])
        else:
            check += 3 * int(isbn[i])
        i += 1    
    return (10 - (check % 10))

isbn = input("To calculate the ISBN check digit, please enter a 12 digit ISBN without dashes ")
while not (isbn.isdigit() and len(isbn) == 12):
    isbn = input("Please enter a 12 digit number without dashes ")

print(f"{isbn}{checksum(isbn)}")
