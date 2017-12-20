from sys import exit

class Player(object):

    def __init__(self, name):
        self.name = name
    

    def select_tool(self):
        print("You can choose one of the following items for your Advanture:")
        print("\nPossible tools:")
        for i in player.tools:
                print("-", i)
        print("What tool do you want?\n-->")
        self.tool =(input())
        print("before if", self.tool)
        if self.tool == "Lighter" or "ligther": #search why its not going to the else if the input is not equal to ligher
            print("in if", self.tool)
        elif self.tool == "Rope":
            print("test2")
        else:
            exit()

    
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
        print("You are in Room 'Tunnel'")
        print(player.tool)
        exit()

class firstRoom(Room):
    def enter(self):
        print("You are in Room:'first room'")
        exit()

class Pit(Room):
    def enter(self):
        print("You are in Room:'Pit'")
        exit()
    
class DiamondRoom(Room):
    def enter(self):
        print("You are in Room:'DiamondRoom'")
        exit()

class DarkTunnel(Room):
    def enter(self):
        print("You are in Room:'DarkTunnel'")
        exit()

class Pool(Room):
    def enter(self):
        print("You are in Room:'Pool'")
        exit()

class Arena(Room):
    def enter(self):
        print("You are in Room:'Arena'")
        exit()

class Staircase(Room):
    def enter(self):
        print("You are in Room:'Staircase'")
        exit()

class Engine(object):
    
    def play(self, next_room):
        if next_room == "Tunnel":
            current_room = Tunnel()
            current_room.enter()

        elif next_room == "firstRoom":
            current_room = firstRoom()
            current_room.enter()

        elif next_room == "Pit":
            current_room = Pit()
            current_room.enter()

        elif next_room == "DiamondRoom":
            current_room = DiamondRoom()
            current_room.enter()

        elif next_room == "DarkTunnel":
            current_room = DarkTunnel()
            current_room.enter()

        elif next_room == "Pool":
            current_room = Pool()
            current_room.enter()

        elif next_room == "Arena":
            current_room = Arena()
            current_room.enter()

        elif next_room == "Staircase":
            current_room = Staircase()
            current_room.enter()

        else:
            print("Something went wrong... not a valid room.")
            exit()



#Other funtions


    

#Debug and test funtions

def show_tools(player):
    print("\nPossible tools:")
    for i in player.tools:
        print("-", i)

def show_weapons(player):
    print("\nPossible weapons:")
    for i in player.weapons:
        print("-", i)


#Main
player = Player(input("Hello Advanturer, whats your Name?\n-->"))
print("Welcome",player.name)
player.select_tool()
game = Engine()
game.play("Tunnel")

# test = Tunnel()
# test.enter()