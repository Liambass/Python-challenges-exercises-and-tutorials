#rudimentary, unoptimised Rubik's cube solver
#initial state must be hard coded
#no validation checks are done on initial state
#if invalid, program will attempt to solve in an infinite loop
#print formatting only valid when colours represented by single digit intergers 

def u(c): #rotates upper face CW
    uface = [[c[0][2][0],c[0][1][0],c[0][0][0]],[c[0][2][1],c[0][1][1],c[0][0][1]],[c[0][2][2],c[0][1][2],c[0][0][2]]]
    rface = [c[5][0],c[1][1],c[1][2]]
    fface = [c[1][0],c[4][1],c[4][2]]
    lface = [c[4][0],c[3][1],c[3][2]]
    bface = [c[3][0],c[5][1],c[5][2]]
    dface = c[2]
    c[6].append("U, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def r(c): #rotates right face CW
    uface = [[c[0][0][0],c[0][0][1],c[4][0][2]],[c[0][1][0],c[0][1][1],c[4][1][2]],[c[0][2][0],c[0][2][1],c[4][2][2]]]
    rface = [[c[1][2][0],c[1][1][0],c[1][0][0]],[c[1][2][1],c[1][1][1],c[1][0][1]],[c[1][2][2],c[1][1][2],c[1][0][2]]]
    fface = [[c[4][0][0],c[4][0][1],c[2][0][2]],[c[4][1][0],c[4][1][1],c[2][1][2]],[c[4][2][0],c[4][2][1],c[2][2][2]]]
    lface = c[3]
    bface = [[c[0][2][2],c[5][0][1],c[5][0][2]],[c[0][1][2],c[5][1][1],c[5][1][2]],[c[0][0][2],c[5][2][1],c[5][2][2]]]
    dface = [[c[2][0][0],c[2][0][1],c[5][2][0]],[c[2][1][0],c[2][1][1],c[5][1][0]],[c[2][2][0],c[2][2][1],c[5][0][0]]]
    c[6].append("R, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def d(c): #rotates down face CW
    uface = c[0]
    rface = [c[1][0],c[1][1],c[4][2]]
    fface = [c[4][0],c[4][1],c[3][2]]
    lface = [c[3][0],c[3][1],c[5][2]]
    bface = [c[5][0],c[5][1],c[1][2]]
    dface = [[c[2][2][0],c[2][1][0],c[2][0][0]],[c[2][2][1],c[2][1][1],c[2][0][1]],[c[2][2][2],c[2][1][2],c[2][0][2]]]
    c[6].append("D, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def l(c): #rotates left face CW
    uface = [[c[5][2][2],c[0][0][1],c[0][0][2]],[c[5][1][2],c[0][1][1],c[0][1][2]],[c[5][0][2],c[0][2][1],c[0][2][2]]]
    rface = c[1]
    fface = [[c[0][0][0],c[4][0][1],c[4][0][2]],[c[0][1][0],c[4][1][1],c[4][1][2]],[c[0][2][0],c[4][2][1],c[4][2][2]]]
    lface = [[c[3][2][0],c[3][1][0],c[3][0][0]],[c[3][2][1],c[3][1][1],c[3][0][1]],[c[3][2][2],c[3][1][2],c[3][0][2]]]
    bface = [[c[5][0][0],c[5][0][1],c[2][2][0]],[c[5][1][0],c[5][1][1],c[2][1][0]],[c[5][2][0],c[5][2][1],c[2][0][0]]]
    dface = [[c[4][0][0],c[2][0][1],c[2][0][2]],[c[4][1][0],c[2][1][1],c[2][1][2]],[c[4][2][0],c[2][2][1],c[2][2][2]]]
    c[6].append("L, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def f(c): #rotates front face CW
    uface = [c[0][0],c[0][1],[c[3][2][2],c[3][1][2],c[3][0][2]]]
    rface = [[c[0][2][0],c[1][0][1],c[1][0][2]],[c[0][2][1],c[1][1][1],c[1][1][2]],[c[0][2][2],c[1][2][1],c[1][2][2]]]
    fface = [[c[4][2][0],c[4][1][0],c[4][0][0]],[c[4][2][1],c[4][1][1],c[4][0][1]],[c[4][2][2],c[4][1][2],c[4][0][2]]]
    lface = [[c[3][0][0],c[3][0][1],c[2][0][0]],[c[3][1][0],c[3][1][1],c[2][0][1]],[c[3][2][0],c[3][2][1],c[2][0][2]]]
    bface = c[5]
    dface = [[c[1][2][0],c[1][1][0],c[1][0][0]],c[2][1],c[2][2]]
    c[6].append("F, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def b(c): #rotates back face CW
    uface = [[c[1][0][2],c[1][1][2],c[1][2][2]],c[0][1],c[0][2]]
    rface = [[c[1][0][0],c[1][0][1],c[2][2][2]],[c[1][1][0],c[1][1][1],c[2][2][1]],[c[1][2][0],c[1][2][1],c[2][2][0]]]
    fface = c[4]
    lface = [[c[0][0][2],c[3][0][1],c[3][0][2]],[c[0][0][1],c[3][1][1],c[3][1][2]],[c[0][0][0],c[3][2][1],c[3][2][2]]]
    bface = [[c[5][2][0],c[5][1][0],c[5][0][0]],[c[5][2][1],c[5][1][1],c[5][0][1]],[c[5][2][2],c[5][1][2],c[5][0][2]]]
    dface = [c[2][0],c[2][1],[c[3][0][0],c[3][1][0],c[3][2][0]]]
    c[6].append("B, ")
    return [uface,rface,dface,lface,fface,bface,c[6]]
def topcross(c): #creates top cross
    c = f(f(f(u(u(u(r(r(r(u(r(f(c))))))))))))
    return c
def topswap(c): #swaps top front edge and top left edge
    c = u(r(r(r(u(u(r(u(r(r(r(u(r(c)))))))))))))
    return c
def toprot(c): #rotates 3 top corners
    c = l(u(u(u(r(r(r(u(l(l(l(u(u(u(r(u(c))))))))))))))))
    return c
def toporient(c): #orients top corners
    c = d(r(d(d(d(r(r(r(c))))))))
    return c

c = [[[0,0,0],[0,0,0],[0,0,0]],[[1,1,1],[1,1,1],[1,1,1]],[[2,2,2],[2,2,2],[2,2,2]],[[3,3,3],[3,3,3],[3,3,3]],[[4,4,4],[4,4,4],[4,4,4]],[[5,5,5],[5,5,5],[5,5,5]],[]]
c = f(r(l(b(u(b(r(r(d(c))))))))) #mixes cube
out = ""

#prints cube
print(f"         {c[0][0]}\n         {c[0][1]}\n         {c[0][2]}\n{c[3][0]}{c[4][0]}{c[1][0]}{c[5][0]}\n{c[3][1]}{c[4][1]}{c[1][1]}{c[5][1]}\n{c[3][2]}{c[4][2]}{c[1][2]}{c[5][2]}\n         {c[2][0]}\n         {c[2][1]}\n         {c[2][2]}\n")


#creates (bad) bottom cross
while not (c[2][0][1]==c[2][1][0]==c[2][1][2]==c[2][2][1]==c[2][1][1]): #checks if bottom cross exists
    while c[2][1][1] in [c[0][0][1],c[0][1][0],c[0][1][2],c[0][2][1]]: #if any bottom edge tiles showing on top face, move to bottom face in correct orientation but not necessarily correct position 
        while c[2][0][1] == c[2][1][1]:
            c = d(c)
        while c[0][2][1] != c[2][1][1]:
            c = u(c)
        c = f(f(c))
    while c[2][1][1] in [c[1][0][1],c[1][1][0],c[1][1][2],c[1][2][1]]: #if any bottom edge tiles showing on right face, move to bottom face in correct orientation but not necessarily correct position 
        while c[2][1][2] == c[2][1][1]:
            c = d(c)
        while c[1][2][1] != c[2][1][1]:
            c = r(c)
        c = f(d(d(d(r(c)))))
    while c[2][1][1] in [c[3][0][1],c[3][1][0],c[3][1][2],c[3][2][1]]: #if any bottom edge tiles showing on left face, move to bottom face in correct orientation but not necessarily correct position 
        while c[2][1][0] == c[2][1][1]:
            c = d(c)
        while c[3][2][1] != c[2][1][1]:
            c = l(c)
        c = b(d(d(d(l(c)))))
    while c[2][1][1] in [c[4][0][1],c[4][1][0],c[4][1][2],c[4][2][1]]: #if any bottom edge tiles showing on front face, move to bottom face in correct orientation but not necessarily correct position 
        while c[2][0][1] == c[2][1][1]:
            c = d(c)
        while c[4][2][1] != c[2][1][1]:
            c = f(c)
        c = l(d(d(d(f(c)))))
    while c[2][1][1] in [c[5][0][1],c[5][1][0],c[5][1][2],c[5][2][1]]: #if any bottom edge tiles showing on back face, move to bottom face in correct orientation but not necessarily correct position 
        while c[2][2][1] == c[2][1][1]:
            c = d(c)
        while c[5][2][1] != c[2][1][1]:
            c = b(c)
        c = r(d(d(d(b(c)))))

#fixes bottom cross
while c[4][2][1] != c[4][1][1]: #ensures front bottom edge is correctly positioned
    c = d(c)
while c[1][2][1] != c[1][1][1]: #if right bottom edge is not correct, rotate positions of right, left, and back bottom edges
    c = l(l(l(d(d(l(d(l(l(l(d(l(c))))))))))))
while c[3][2][1] != c[3][1][1]: #if left bottom edge is not correct, swap positions of left and back bottom edge
    c = d(r(r(r(d(d(r(d(r(r(r(d(r(c)))))))))))))

#completes bottom layer
while c[2][0][0] != c[2][1][1] or c[2][0][1] != c[2][1][1] or c[2][2][0] != c[2][1][1] or c[2][2][2] != c[2][1][1] or c[1][2][0] != c[1][2][1] or c[3][2][0] != c[3][2][1] or c[4][2][0] != c[4][2][1] or c[5][2][0] != c[5][2][1]:
    while c[2][1][1] in [c[0][0][0],c[0][0][2],c[0][2][0],c[0][2][2]]: #moves any bottom corner panels showing on top face to correct position and orientation relative to bottom edge pieces
        while c[0][2][2] != c[2][1][1]:
            c = u(c)
        while c[4][0][2] != c[1][2][1]:
            c = d(c)
        c = r(r(r(b(b(b(u(u(b(r(c))))))))))
    while c[2][1][1] in [c[1][0][2],c[3][0][2],c[4][0][2],c[5][0][2]]: #moves any bottom corner panels showing on right edges of top layer faces to correct position and orientation relative to bottom edge pieces
        while c[4][0][2] != c[2][1][1]:
            c = u(c)
        while c[1][0][0] != c[1][2][1]:
            c = d(c)
        c = f(u(u(u(f(f(f(c)))))))
    while c[2][1][1] in [c[1][0][0],c[3][0][0],c[4][0][0],c[5][0][0]]: #moves any bottom corner panels showing on left edges of top layer faces to correct position and orientation relative to bottom edge pieces
        while c[4][0][0] != c[2][1][1]:
            c = u(c)
        while c[3][0][2] != c[3][2][1]:
            c = d(c)
        c = f(f(f(u(f(c)))))
    while c[2][1][1] in [c[1][2][2],c[3][2][2],c[4][2][2],c[5][2][2]]: #moves any bottom corner panels showing on right edges of bottom layer to top layer to be dealth with on next "complete bottom layer" loop
        while c[4][2][2] != c[2][1][1]:
            c = d(c)
        c = r(r(r(u(r(c)))))
    while c[2][1][1] in [c[1][2][0],c[3][2][0],c[4][2][0],c[5][2][0]]: #moves any bottom corner panels showing on left edges of bottom layer to top layer to be dealth with on next "complete bottom layer" loop
        while c[1][2][0] != c[2][1][1]:
            c = d(c)
        c = r(r(r(u(r(c)))))
    for _ in range(4): #checks any bottom corner panels showing on bottom face are in the correct position relative to bottom edge pieces, any incorrect pieces moved to top layer to be dealt with on next "complete bottom layer" loop
        if c[1][2][0] != c[1][2][1] and c[2][0][2] == c[2][1][1]:
            c = r(r(r(u(r(c)))))
        c = d(c)
while c[4][2][1] != c[4][1][1]: #correctly orientates bottom layer reative to other sides
    c = d(c)

#completes middle layer
while c[4][1][2] != c[4][1][1] or c[4][1][0] != c[4][1][1] or c[1][1][2] != c[1][1][1] or c[1][1][0] != c[1][1][1] or c[3][1][2] != c[3][1][1] or c[3][1][0] != c[3][1][1] or c[5][1][2] != c[5][1][1] or c[5][1][0] != c[5][1][1]:
    if c[4][1][2] == c[1][1][1] and c[1][1][0] == c[4][1][1]: #corrects orientation if front right piece is correctly placed but backwards
        c = f(u(f(f(f(u(u(u(r(r(r(u(u(u(r(u(u(u(f(u(f(f(f(u(u(u(r(r(r(u(u(u(r(c)))))))))))))))))))))))))))))))))
    if c[1][1][2] == c[5][1][1] and c[5][1][0] == c[1][1][1]: #corrects orientation if right right piece is correctly placed but backwards
        c = r(u(r(r(r(u(u(u(b(b(b(u(u(u(b(u(u(u(r(u(r(r(r(u(u(u(b(b(b(u(u(u(b(c)))))))))))))))))))))))))))))))))
    if c[5][1][2] == c[3][1][1] and c[3][1][0] == c[5][1][1]: #corrects orientation if back right piece is correctly placed but backwards
        c = b(u(b(b(b(u(u(u(l(l(l(u(u(u(l(u(u(u(b(u(b(b(b(u(u(u(l(l(l(u(u(u(l(c)))))))))))))))))))))))))))))))))
    if c[3][1][2] == c[4][1][1] and c[4][1][0] == c[3][1][1]: #corrects orientation if left right piece is correctly placed but backwards
        c = l(u(l(l(l(u(u(u(f(f(f(u(u(u(f(u(u(u(l(u(l(l(l(u(u(u(f(f(f(u(u(u(f(c)))))))))))))))))))))))))))))))))
    for _ in range(4): #places all middle layer edges from top layer
        if c[4][0][1] == c[4][1][1] and c[0][2][1] == c[1][1][1]: #places front right edge if possible
            c = f(u(f(f(f(u(u(u(r(r(r(u(u(u(r(u(c))))))))))))))))
        if c[4][0][1] == c[4][1][1] and c[0][2][1] == c[3][1][1]: #places front left edge if possible
            c = f(f(f(u(u(u(f(u(l(u(l(l(l(u(u(u(c))))))))))))))))
        if c[1][0][1] == c[1][1][1] and c[0][1][2] == c[5][1][1]: #places right right edge if possible
            c = r(u(r(r(r(u(u(u(b(b(b(u(u(u(b(u(c))))))))))))))))
        if c[1][0][1] == c[1][1][1] and c[0][1][2] == c[4][1][1]: #places right left edge if possible
            c = r(r(r(u(u(u(r(u(f(u(f(f(f(u(u(u(c))))))))))))))))
        if c[5][0][1] == c[5][1][1] and c[0][0][1] == c[3][1][1]: #places back right edge if possible
            c = b(u(b(b(b(u(u(u(l(l(l(u(u(u(l(u(c))))))))))))))))
        if c[5][0][1] == c[5][1][1] and c[0][0][1] == c[1][1][1]: #places back left edge if possible
            c = b(b(b(u(u(u(b(u(r(u(r(r(r(u(u(u(c))))))))))))))))
        if c[3][0][1] == c[3][1][1] and c[0][1][0] == c[4][1][1]: #places left right edge if possible
            c = l(u(l(l(l(u(u(u(f(f(f(u(u(u(f(u(c))))))))))))))))
        if c[3][0][1] == c[3][1][1] and c[0][1][0] == c[5][1][1]: #places left left edge if possible
            c = l(l(l(u(u(u(l(u(b(u(b(b(b(u(u(u(c))))))))))))))))
        c = u(c)
    if c[4][1][2] != c[4][1][1] or c[1][1][0] != c[1][1][1]: #moves front right edge to top layer if wrong to be dealt with on next "complete middle layer" loop
        c = f(u(f(f(f(u(u(u(r(r(r(u(u(u(r(u(c))))))))))))))))
    elif c[1][1][2] != c[1][1][1] or c[5][1][0] != c[5][1][1]: #else moves right right edge to top layer if wrong to be dealt with on next "complete middle layer" loop
        c = r(u(r(r(r(u(u(u(b(b(b(u(u(u(b(u(c))))))))))))))))
    elif c[5][1][2] != c[5][1][1] or c[3][1][0] != c[3][1][1]: #else moves back right edge to top layer if wrong to be dealt with on next "complete middle layer" loop
        c = b(u(b(b(b(u(u(u(l(l(l(u(u(u(l(u(c))))))))))))))))
    elif c[3][1][2] != c[3][1][1] or c[4][1][0] != c[4][1][1]: #else moves left right edge to top layer if wrong to be dealt with on next "complete middle layer" loop
        c = l(u(l(l(l(u(u(u(f(f(f(u(u(u(f(u(c))))))))))))))))

#completes (bad) top cross
while c[0][0][1] != c[0][1][1] or c[0][1][0] != c[0][1][1] or c[0][1][2] != c[0][1][1] or c[0][2][1] != c[0][1][1]: 
    if c[0][0][1] != c[0][1][1] and c[0][1][0] != c[0][1][1] and c[0][1][2] != c[0][1][1] and c[0][2][1] != c[0][1][1]: #if "dot", creates "Г" shape
        c = topcross(c)
    while not ((c[0][1][0] == c[0][1][1]) and (c[0][0][1] == c[0][1][1] or c[0][1][2] == c[0][1][1])): #rotates top until horizontal line or "⅃" shape
        c = u(c)
    c = topcross(c) #creates line from "⅃" , or + from line

#fixes top cross
while c[4][0][1] != c[4][1][1] or c[1][0][1] != c[1][1][1] or c[3][0][1] != c[3][1][1] or c[5][0][1] != c[5][1][1]:
    while c[4][0][1] != c[4][1][1]: #ensures front top edge is correctly positioned
        c = u(c)
    if (c[5][0][1] == c[5][1][1] and c[3][0][1] == c[1][1][1]) or (c[5][0][1] == c[1][1][1] and c[3][0][1] == c[3][1][1]):
        c = u(u(topswap(u(u(c)))))
    if c[5][0][1] == c[1][1][1] and c[3][0][1] == c[5][1][1]:
        c = topswap(u(c))
    if c[5][0][1] == c[3][1][1] and c[3][0][1] == c[5][1][1]:
        c = topswap(u(u(u(c))))
    if c[5][0][1] == c[3][1][1] and c[3][0][1] == c[1][1][1]:
        c = topswap(c)

#places top corners
z = 0
while not all(x in [c[0][1][1], c[4][0][1], c[1][0][1]] for x in [c[0][2][2], c[4][0][2], c[1][0][0]]): #rotates top layer until finding a corner piece correctly placed with respect to top edges and places it right front  
    c = u(c)
    z += 1
    if z == 4: #if no correct corner piece found after complete spin toprot algorithm ensures one will be found on next spin  
        c = toprot(c)
        z = 0
while not all(x in [c[0][1][1], c[5][0][1], c[1][0][1]] for x in [c[0][0][2], c[1][0][2], c[5][0][0]]): #if right back corner is not correct runs toprot algorithm until it is. If front right and back right are correct then all must be. 
    c = toprot(c)

#orients top corners
while not c[0][0][0] == c[0][0][2] == c[0][2][0] == c[0][2][2] == c[0][1][1]:
    while c[0][2][2] == c[0][1][1]:
        c = u(c)
    while c[0][2][2] != c[0][1][1]:
        c = toporient(c)

while c[4][0][1] != c[4][1][1]: #ensures top layer is correctly positioned
    c = u(c)


#prints cube
print(f"         {c[0][0]}\n         {c[0][1]}\n         {c[0][2]}\n{c[3][0]}{c[4][0]}{c[1][0]}{c[5][0]}\n{c[3][1]}{c[4][1]}{c[1][1]}{c[5][1]}\n{c[3][2]}{c[4][2]}{c[1][2]}{c[5][2]}\n         {c[2][0]}\n         {c[2][1]}\n         {c[2][2]}\n")

out = "".join(c[6]) #creates string of solution
while "U, U, U, U, " in out or "D, D, D, D, " in out or "L, L, L, L, " in out or "R, R, R, R, " in out or "F, F, F, F, " in out or "B, B, B, B, " in out:
    for i in ["U","D","L","R","F","B"]: #removes redundant moves
        out = out.replace(f"{i}, {i}, {i}, {i}, ", "") 
for i in ["U","D","L","R","F","B"]: #formats solution
    out = out.replace(f"{i}, {i}, {i}, ", f"{i}', ") #condenses "<move>, <move>, <move>, " to "<move>' "
    out = out.replace(f"{i}, {i}, ", f"{i}2, ") #condenses "<move>, <move>, " to "<move>2 "

#prints solution
print(out)

