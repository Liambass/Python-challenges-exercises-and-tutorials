#Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.
# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.
# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

name = input("Name? ")
hw = int(input("Homework score? (/25) "))
ass = int(input("Assessment score? (/50) "))
exam = int(input("Exam score? (/100) "))

def weighted_score(fhw = 0, fass = 0, fexam = 0):
    percentage = (fhw + fass + fexam)*100/175
    return percentage

#print(f"{name} {round(weighted_score(hw, ass, exam), 2)} percent")

score = weighted_score(hw, ass, exam)

if score > 90:
    print(f"{name}: A*")
elif score > 85:
    print(f"{name}: A")
elif score > 80:
    print(f"{name}: B")
elif score > 75:
    print(f"{name}: C")
elif score > 70:
    print(f"{name}: D")
elif score > 65:
    print(f"{name}: E")
elif score > 60:
    print(f"{name}: F")
else:
    print(f"{name}: U")