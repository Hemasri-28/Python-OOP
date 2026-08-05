#method overriding is when a child class provides its own implementation of a method that already exists in the parent class
#super keyword can also be used
class Animal:
    def speak(self):
        print("Animals make sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()
dog=Dog()
dog.speak()