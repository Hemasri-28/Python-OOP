# @classmethod take (cls) as the first parameter, which represents the class itself
class Student:
    count=0
    def __init__(self,name, gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
    #Instanace method
    def get_details(self):
        return f"{self.name}, {self.gpa}"
    #Class method
    @classmethod
    def get_count(cls):
        return f"Total no. of Students: {cls.count}"
student1=Student("Hemasri",8.0)
student1=Student("Bob",9.0)
student1=Student("Melon",7.0)
print(student1.get_details())
print(Student.get_count())