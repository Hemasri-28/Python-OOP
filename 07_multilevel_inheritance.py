#inherit from a parent which inherits from another parent
#a parent can inherit from another parent
#animal --> mammal --> dog
class Animal: #Grandparent
    def eat(self):
        print("Animal eats food")
class Dog(Animal): #Parent
    def bark(self):
        print("Dog barks")
class Puppy(Dog): #Child
    def weep(self):
        print("Puppy weeps")
puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.weep()