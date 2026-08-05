# It 'owns-a' relationship
# The composed object directly owns its components, which cannot exit independently
# Child object cannot exist independently of the parent object
class Engine:
    def start(self):
        print("Engine started")
class Wheel:
    def rotate(self):
        print("Wheels are rotating")
class Car:
    def __init__(self, company):
        self.company = company
        self.engine = Engine()
        self.wheels = Wheel()
    def drive(self):
        print(f"{self.company} is ready to drive")
        self.engine.start()
        self.wheels.rotate()
        print("Car is moving")
car = Car("Swift")
car.drive() 