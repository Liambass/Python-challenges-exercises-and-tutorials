def printmaze(m): #prints a formatted maze
    for i in range(len(m)):
        print("".join(m[i]))

def validate(m): #ensures maze is valid and returns initial position and orientation of explorer
    l = len(m[0])
    exits = 0
    explorers = 0
    p = []
    for i in range(len(m)):
        if len(m[i]) != l:
            print("your maze is not rectangular. The program will now close.")
            exit()
    for i in m[0]:
        if not i in ["#","E"]:
            print("The perimeter of your maze contains invalid characters. The program will now close.")
            exit()
    for i in m[-1]:
        if not i in ["#","E"]:
            print("The perimeter of your maze contains invalid characters. The program will now close.")
            exit()
    for i in range(len(m)):
        if not m[i][0] in ["#","E"]:
            print("The perimeter of your maze contains invalid characters. The program will now close.")
            exit()
        if not m[i][-1] in ["#","E"]:
            print("The perimeter of your maze contains invalid characters. The program will now close.")
            exit()
    for i in range(len(m)):
        for j in range(l):
            if m[i][j] == "E":
                exits += 1
            if m[i][j] in ["^","v","<",">"]:
                explorers += 1
                p = [i,j,m[i][j]]
            if not m[i][j] in ["^","v","<",">","#","E"," "]:
                print("Your maze contains invalid characters. The program will now close.")
                exit()
    if exits == 0:
        print("Your maze has no exits. The program will now close.")
        exit()
    if explorers != 1:
        print("Your maze does not have exactly 1 explorer. The program will now close.")
        exit()
    return p

def sixsteps(m, p):
    i = 0
    while i < 6:
        if p[2] == "^":
            if m[p[0]-1][p[1]] == "E": #next space is exit
                m[p[0]][p[1]] = " "
                m[p[0]-1][p[1]] = "!"
                printmaze(m)
                print("Your explorer escaped!!")
                exit()
            elif m[p[0]-1][p[1]] == " ": #next space is empty
                m[p[0]][p[1]] = " "
                m[p[0]-1][p[1]] = "^"
                p[0] = p[0]-1
                i += 1
                if i == 6:
                    m[p[0]][p[1]] = "v"
                    p[2] = "v"
            elif m[p[0]-1][p[1]] == "#": #next space is wall
                if m[p[0]][p[1]+1] != "#":
                    m[p[0]][p[1]] = ">"
                    p[2] = ">"
                elif m[p[0]][p[1]-1] != "#":
                    m[p[0]][p[1]] = "<"
                    p[2] = "<"
                else:
                    m[p[0]][p[1]] = "v"
                    p[2] = "v"
        elif p[2] == "v":
            if m[p[0]+1][p[1]] == "E": #next space is exit
                m[p[0]][p[1]] = " "
                m[p[0]+1][p[1]] = "!"
                printmaze(m)
                print("Your explorer escaped!!")
                exit()
            elif m[p[0]+1][p[1]] == " ": #next space is empty
                m[p[0]][p[1]] = " "
                m[p[0]+1][p[1]] = "v"
                p[0] = p[0]+1
                i += 1
                if i == 6:
                    m[p[0]][p[1]] = "^"
                    p[2] = "^"
            elif m[p[0]+1][p[1]] == "#": #next space is wall
                if m[p[0]][p[1]-1] != "#":
                    m[p[0]][p[1]] = "<"
                    p[2] = "<"
                elif m[p[0]][p[1]+1] != "#":
                    m[p[0]][p[1]] = ">"
                    p[2] = ">"
                else:
                    m[p[0]][p[1]] = "^"
                    p[2] = "^"
        elif p[2] == "<":
            if m[p[0]][p[1]-1] == "E": #next space is exit
                m[p[0]][p[1]] = " "
                m[p[0]][p[1]-1] = "!"
                printmaze(m)
                print("Your explorer escaped!!")
                exit()
            elif m[p[0]][p[1]-1] == " ": #next space is empty
                m[p[0]][p[1]] = " "
                m[p[0]][p[1]-1] = "<"
                p[1] = p[1]-1
                i += 1
                if i == 6:
                    m[p[0]][p[1]] = ">"
                    p[2] = ">"
            elif m[p[0]][p[1]-1] == "#": #next space is wall
                if m[p[0]-1][p[1]] != "#":
                    m[p[0]][p[1]] = "^"
                    p[2] = "^"
                elif m[p[0]+1][p[1]] != "#":
                    m[p[0]][p[1]] = "v"
                    p[2] = "v"
                else:
                    m[p[0]][p[1]] = ">"
                    p[2] = ">"
        elif p[2] == ">":
            if m[p[0]][p[1]+1] == "E": #next space is exit
                m[p[0]][p[1]] = " "
                m[p[0]][p[1]+1] = "!"
                printmaze(m)
                print("Your explorer escaped!!")
                exit()
            elif m[p[0]][p[1]+1] == " ": #next space is empty
                m[p[0]][p[1]] = " "
                m[p[0]][p[1]+1] = ">"
                p[1] = p[1]+1
                i += 1
                if i == 6:
                    m[p[0]][p[1]] = "<"
                    p[2] = "<"
            elif m[p[0]][p[1]+1] == "#": #next space is wall
                if m[p[0]+1][p[1]] != "#":
                    m[p[0]][p[1]] = "v"
                    p[2] = "v"
                elif m[p[0]-1][p[1]] != "#":
                    m[p[0]][p[1]] = "^"
                    p[2] = "^"
                else:
                    m[p[0]][p[1]] = "<"
                    p[2] = "<"
    return m, p

m = [] #maze
p = [] #current position and orientation of explorer
h = [] #history of explorer position and orientation after each cycle of moves

print("Please enter your maze.\nWalls are signified by \"#\".\nExits are signified by \"E\".\nThe Explorer is signified by \"^\", \"v\", \"<\" or \">\" depending on the direction he is facing.\nOpen spaces are signified by \" \".\nYour maze must be rectangular; each row must be the same length.\nThe first and last row must only contain \"#\" and \"E\", all other rows must start and end with a \"#\" or \"E\".")
r = int(input("How many rows is your maze? "))
for i in range(r): #accepts maze input
    if i == 0:
        m.append(list(input("Please enter the first row of your maze: ")))
    elif i == r-1:
        m.append(list(input("Please enter the last row of your maze:  ")))
    else:
        m.append(list(input("Please enter the next row of your maze:  ")))

printmaze(m)
p = validate(m)
h.append([p[0],p[1],p[2]])

while True: #maximum loop of count(" ")*4 + 3
    m, p = sixsteps(m, p)

    if p in h: #if explorer finishes a cycle of moves in a position and orientation that he previously started a cycle in then he is stuck in a loop and therefore trapped
        m[p[0]][p[1]] = "X"
        printmaze(m)
        print("Your explorer is trapped!")
        exit()

    h.append([p[0],p[1],p[2]])
    printmaze(m)


