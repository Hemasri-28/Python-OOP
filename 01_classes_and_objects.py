#A class defines what an object should look like and an object is created based on the class
#A class is a blueprint
class Car:#This is a class
    def __init__(self,model,color):#constructor,defining attributes
        self.model=model
        self.color=color
    def drive(self):#method
        print(f"Drive the {self.model}")
    def stop(self):#metod
        print(f"Stop the {self.model}")
    def describe(self):#method
        print(f"The car name is {self.model} and its color is {self.color}")
car1=Car("Volkwagen", "Red")#Object
car2=Car("XUV 500","White")#Object
print(car1.model)
print(car1.color)
print(car2.model)
print(car2.color)
car1.describe()
car2.describe()
car1.drive()
car2.stop()