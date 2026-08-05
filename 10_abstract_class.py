#a class that cannot be instantiated on its own 
#contains abstract methods, which are declared but have no implementation
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bow!")
dog=Dog()
dog.speak()