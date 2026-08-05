#It allows same method name to perform different actions depending on the object
#using inheritance
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping
class Square(Shape):
    def __init__(self,width):
        self.width=width
    def area(self):
        return self.width * self.width
shapes=[Circle(4),Pizza("Chicken",10),Square(14)]
for shape in shapes:
    print(f"{shape.area()}cm^2")