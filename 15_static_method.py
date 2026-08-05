# A static method is a method that belongs to a class but does not use self. 
# It performs a task related to the class without accessing object or class data.
class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    @staticmethod
    def is_valid_position(position):
        valid_positions=["HR","Manager","Cashier"]
        return position in valid_positions
print(Employee.is_valid_position("HR"))
print(Employee.is_valid_position("employee"))