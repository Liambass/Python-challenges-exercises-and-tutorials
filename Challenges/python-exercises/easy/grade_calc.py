
def gradecalc(m,c,p):
    percent = round((int(m)+int(c)+int(p))/3,2)
    if percent >= 70:
        return f"Your percentage score was: {percent}%\nYou scored a grade of: A"
    elif percent >= 60:
        return f"Your percentage score was: {percent}%\nYou scored a grade of: B"
    elif percent >= 50:
        return f"Your percentage score was: {percent}%\nYou scored a grade of: C"
    elif percent >= 40:
        return f"Your percentage score was: {percent}%\nYou scored a grade of: D"
    else:
        return f"You failed with a percentage score of: {percent}%"


m = input("Maths mark? ")
while not (0 <= int(m) <= 100):
    m = input("Please enter a valid mark between 0 and 100 ")

c = input("Chem mark? ")
while not (0 <= int(c) <= 100):
    m = input("Please enter a valid mark between 0 and 100 ")

p = input("Physics mark? ")
while not (0 <= int(p) <= 100):
    m = input("Please enter a valid mark between 0 and 100 ")

print(gradecalc(m,c,p))

