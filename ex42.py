class Animal(object):
    
    def __init__(self, name):
        self.name = name

    def test(self):
        print("test")


class Dog(Animal):

    race = "Dog"

    def __init__(self, name, dog_race):
        super().__init__(name)
        self.dog_race = dog_race


class Cat(Animal):

    race = "Cat"


class Fish(Animal):

    race = "Fish"


class Salmon(Fish):
    
    race = "Salmon"

class Halibut(Fish):
    
    race = "Halibut"

class Person(object):

    def __init__(self, name):
        self.name = name

    def test2(self, culo):
        print(culo)

class Pet_owner(Person):

    def __init__(self, name, pet = None):
        super().__init__(name)
        #If no Pet is given than pet=None
        if pet is None:
            self.pet = []
        else:
            self.pet = pet
    
    def add_pet(self, pet_name):
        if pet_name not in self.pet:
            self.pet.append(pet_name)
    
    def remove_pet(self, pet_name):
        if pet_name in self.pet:
            self.pet.remove(pet_name)
    
    def print_pets(self):
        for pets in self.pet:
            print("-->",pets.race)
            print("-->",pets.name)
            #print("-->",pets.dog_race)

#Creating Animals (No fish for the moment)
rover = Dog("Rover", "pinche")
satan = Cat("Satan",)
timmy = Dog("Timmy", "Pastor")
blubi = Halibut("Blubi")

#Creating the Persons
mary = Pet_owner("Mary", [rover])
frank = Person("Frank")
marius = Pet_owner("Marius", [timmy])

#Testing Stuff
print("Marius has a Pet with the following attributes:")
marius.print_pets()
print("Add Rover")
marius.add_pet(rover)
marius.print_pets()
print("Remove Timmy")
marius.remove_pet(timmy)
marius.print_pets()
print("Remove Rover")
marius.remove_pet(rover)
marius.print_pets()
rover.test()
marius.test2("culo2")