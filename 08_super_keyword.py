#used to reuse the constructor of a parent class(super class) in child class(sub class)
class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width
circle=Circle("Red",True,10)
square=Square("Green",False,28)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
print(square.color)
print(square.is_filled)
print(square.width)