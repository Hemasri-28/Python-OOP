#child class inherits from more than one parent class
class Prey: #parent
    def flee(self):
        print("This animal is fleeing")
class Predator: #parent
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey): #child
    pass
class Hawk(Predator): #child
    pass
class Fish(Prey,Predator): #child
    pass
rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()