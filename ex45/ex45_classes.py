from sys import exit

class Player(object):

    def __init__(self, name):
        self.name = name
    
    tools={
        "Lighter",
        "Rope",
        "Bottle_of_water"
    }

    weapons={
        "Sword",
        "Crossbow",
        "Shield",
        "Spear"
    }

class Room(object):
    pass

class Tunnel(Room):

    def enter(self):
        print(f"{player.name} is in a tunnel and finds door")
        exit()


class firstRoom(Room):
    pass

class Pit(Room):
    pass

class DiamondRoom(Room):
    pass

class DarkTunnel(Room):
    pass

class Pool(Room):
    pass

class Arena(Room):
    pass

class Staircase(Room):
    pass

class Engine(object):
    pass



player = Player(input("Enter your Name:"))
print ("Player Name:", player.name)
print("\nPossible tools:")
for i in player.tools:
    print("-", i)
print("\nPossible weapons:")
for i in player.weapons:
    print("-", i)
test = Tunnel()
test.enter()