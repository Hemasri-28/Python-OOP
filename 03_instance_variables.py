#instance variables are defined inside the constructor
#belong to an object
class Car:
    def __init__(self, model, color):
        # Instance variables
        self.model = model
        self.color = color

car1 = Car("Volkswagen", "Red")
car2 = Car("XUV 500", "White")

print(car1.model)  # Volkswagen
print(car2.color)  # White