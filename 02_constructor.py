# __init__() is the constructor in Python.
# It is called automatically when an object is created.
# A constructor initializes the object's attributes.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)

print(student1.name)
print(student1.age)