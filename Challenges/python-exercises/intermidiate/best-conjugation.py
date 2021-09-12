import pdb

def subwords(word):
    #pdb.set_trace()
    out = []
    file = open("wordlist.txt", "r")
    for line in file.readlines():
        if (line[:-1].lower() in word.lower()) and (line != "\n"):
            out.append(line[:-1].title())
    file.close()
    out = ", ".join(out)
    return f"{word.title()} contains the following subwords: {out}"


word = input("For which word would you like top find subwords? ")
print(subwords(word))
