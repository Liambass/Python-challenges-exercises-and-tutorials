#Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

names = []
for i in range(5):
    name = input("name " + str(i+1) +"? ")
    names.append(name)

for name in names:
    print(name + " is awesome!")

