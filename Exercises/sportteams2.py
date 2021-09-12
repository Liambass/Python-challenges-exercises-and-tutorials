# Create a new Python file which does the following:
# - Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
#  -Print out the edited file line by line.

name = input("filename? ")

file = open(f"{name}.txt", "w")
file.write("This Team\nThat Team\nThe Other Team\nYet Another Team\nLast Team")
file.close()

file = open("teams.txt", "r+")
lines = file.readlines()
file.seek(0)
file.write("This is a new line\n")
for i in lines:
    file.write(i)
file.seek(0)
print(file.read())
file.close()