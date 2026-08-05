#Allows a class to inherit attributes and methods from another class
#Helps with code reuseability and extensibility
#has only single parent
#class parent
#class child(parent)
class Animal: #Parent
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal): #Child
    def speak(self):
        print("Woof!")
class Cat(Animal): #Child
    def speak(self):
        print("Meow")
dog=Dog("Scooby")
cat=Cat("Leo")
print(dog.name)
print(cat.name)
print(dog.is_alive)
dog.speak()
cat.speak()
dog.eat()
print(cat.is_alive)