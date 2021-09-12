# Create a Python file which does the following:
# - Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# - Reads and displays the names of the 1st and 4th team in the file.

file = open("teams.txt", "w")
file.write("This Team\nThat Team\nThe Other Team\nYet Another Team\nLast Team")
file.close()

file = open("teams.txt", "r")
outfile = ""
for line in range(1,6):
    if line == 1 or line == 4:
        outfile += file.readline()
    else:
        file.readline()

print(outfile)
file.close()
