
def near(long, short):
    if (len(long) - len(short)) != 1:
        return False
    else:
        lists = list(short.lower())
        i=0
        while i < len(long):
            listl = list(long.lower())
            listl.pop(i)
            if listl == lists:
                return True
            i += 1
        return False

short = input("What word are you trying to find? ")
long = input("What word would you like to check against? ")

print(near(long, short))