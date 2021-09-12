# These challenges are intended to provide practice in basic python skills such as string manipulation, iteration, use of collection types and conditionals

# Challenge 1: Write a function which:
# - Takes a string as an argument
# - returns the string in all upper case if its' length is even, and all lower case if its' length is odd. Any non-alphabetic characters should not be changed
# - stretch goal: try to implement this both with and without the .upper()/.lower() methods

def func_1_methods(string):
    if len(string) % 2 == 0:
        return string.upper()
    else:
        return string.lower()

def func_1_no_methods(string):
    chars = list(string)
    charsout = []
    for char in chars:
        if len(chars) % 2 == 0:
            charsout.append(char.capitalize())
        else:
            charsout.append(char.casefold())
    return "".join(charsout)

# Challenge 2: write a function which:
# - takes a word and a list of words as input
# - returns a new list containing only the words from the given list which differ from the given word in exactly one position
# You should ignore case

def func_2(string, list):
    listl = []
    for word in list:
        listl.append(word.lower())
    stringl = string.lower()

    out = []
    k = 0
    while k < len(list):
        j = 0
        i = 0
        while i < len(string):
            if listl[k][i] == stringl[i]:
                j += 1
            i += 1
        if j == (len(string) - 1):
            out.append(list[k])
        k += 1
    return out


# Challenge 3: write a function which:
# - takes two ints and a list of ints as arguments
# - returns a list of bools where the ith element is True if list[i] has the two given ints as factors and false otherwise

def func_3(int1, int2, intlist):
    out = []
    for int in intlist:
        if (int % int1 == 0) and (int % int2 == 0):
            out.append(True)
        else:
            out.append(False)
    return out

# Challenge 4: write a function which:
# - takes a string as an argument
# - returns a new string containing only the letters from the original string which are at an even-numbered position in the alphabet (letting a = 1, b = 2, ...)
# - the returned string should only contain letter characters. All chars in the returned string should be lower case

def func_4(string):
    allowed = ["b","d","f","h","j","l","n","p","r","t","v","x","z"]
    teststr = string.lower()
    out = ""
    for char in teststr:
        if char in allowed:
            out += char
    return out

# Challenge 5: write a function which:
# - takes a list of integers as argument
# - for each int, creates a list of the factors of the number, including 1 but excluding the number itself
# - converts these lists to strings and writes them out to a csv file called factors.csv, each on a new line
# - note: this function should be a void (i.e return nothing)

def func_5(list):
    file = open("factors.csv", "w")
    for num in list:
        out = []
        i = 1
        while i < num:
            if num % i == 0:
                out.append(str(i))
            i += 1
        out = ",".join(out)
        out += "\n"
        file.write(out)
    file.close()
