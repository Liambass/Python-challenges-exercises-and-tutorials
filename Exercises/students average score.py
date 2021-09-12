# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.


class Student:

    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def avscore(self, test1, test2, test3):
        return f"{self.name}'s average score was {round((test1 + test2 + test3)/3,2)}"

John = Student("John", "21")
Jane = Student("Jane", "22")

jo1 = int(input("John's test 1 score? "))
jo2 = int(input("John's test 2 score? "))
jo3 = int(input("John's test 3 score? "))

ja1 = int(input("Jane's test 1 score? "))
ja2 = int(input("Jane's test 2 score? "))
ja3 = int(input("Jane's test 3 score? "))

print(John.avscore(jo1, jo2, jo3))
print(Jane.avscore(ja1, ja2, ja3))

