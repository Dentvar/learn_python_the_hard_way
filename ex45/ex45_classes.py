from sys import exit

class Player(object):

    def __init__(self, name):
        self.name = name
    

    def select_tool(self):
        print("You can choose one of the following items for your Advanture:")
        print("\nPossible tools:")
        # List the items of the tools list
        for i in player.tools:
            print("-", i)

        print("What tool do you want?\n-->")
        self.tool = str.lower((input()))

        # check if input is correct
        if self.tool != "lighter" and self.tool != "rope" and self.tool != "bottle of water":
            print("Does not compute. Try again")
            self.select_tool()
        else:
            # if input is correct just go on.
            pass

    def select_weapon(self):
        print("You can choose one of the following Weapons:")
        print("\nPossible Weapons:")

        # List the items of the weapons list
        for i in player.weapons:
            print("-", i)

        print("What Weapon do you choose?\n-->")
        self.weapon = str.lower((input()))

        # check if input is correct
        if self.weapon != "sword" and self.weapon != "crossbow" and self.weapon != "shield" and self.weapon != "spear":
            print("Does not compute. Try again")
            self.select_weapon()
        else:
            # if input is correct just go on.
            pass           
    
    tools={
        "lighter",
        "rope",
        "bottle of water"
    }

    weapons={
        "sword",
        "crossbow",
        "shield",
        "spear"
    }

class Room(object):
    pass
    # rooms={
    #     "tunnel": tunnel(),
    #     "first room": tunnel(),
    #     "pit": tunnel(),
    #     "diamond room": tunnel(),
    #     "dark dunnel": tunnel(),
    #     "pool": tunnel(),
    #     "arena": tunnel(),
    #     "staircase": tunnel()
    # }

class Tunnel(Room):

    def enter(self):
        print("You are in Room 'tunnel'")
        play("first room")

class firstRoom(Room):
    def enter(self):
        print("You are in Room:'first room'")
        exit()

class Pit(Room):
    def enter(self):
        print("You are in Room:'pit'")
        exit()
    
class DiamondRoom(Room):
    def enter(self):
        print("You are in Room:'diamondroom'")
        exit()

class DarkTunnel(Room):
    def enter(self):
        print("You are in Room:'darktunnel'")
        exit()

class Pool(Room):
    def enter(self):
        print("You are in Room:'pool'")
        exit()

class Arena(Room):
    def enter(self):
        player.select_weapon()
        print("You are in Room:'arena'")
        exit()

class Staircase(Room):
    def enter(self):
        print("You are in Room:'staircase'")
        exit()

#Other funtions

def play(next_room):

        if next_room == "tunnel":
            current_room = Tunnel()
            current_room.enter()

        elif next_room == "first room":
            current_room = firstRoom()
            current_room.enter()

        elif next_room == "pit":
            current_room = Pit()
            current_room.enter()

        elif next_room == "diamond room":
            current_room = DiamondRoom()
            current_room.enter()

        elif next_room == "dark tunnel":
            current_room = DarkTunnel()
            current_room.enter()

        elif next_room == "pool":
            current_room = Pool()
            current_room.enter()

        elif next_room == "arena":
            current_room = Arena()
            current_room.enter()

        elif next_room == "staircase":
            current_room = Staircase()
            current_room.enter()

        else:
            print("Something went wrong... not a valid room.")
            exit()


#Debug and test funtions


#Main
player = Player(input("Hello Advanturer, whats your Name?\n-->"))
print("Welcome",player.name)
player.select_tool()
play("tunnel")
