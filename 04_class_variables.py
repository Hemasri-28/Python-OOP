#class variables are shared among all instances of a class
#defined outside the constructor
class Student:
    class_year=2026 #class variable
    num_students=0 #class variable
    def __init__(self,name):
        self.name=name
        Student.num_students+=1
student1=Student("Hemasri")
student2=Student("Alice")
Students=[student1,student2]
print(f"Students of {Student.class_year} include:")
for student in Students:
    print(student.name)
print(f"Total:{Student.num_students}")