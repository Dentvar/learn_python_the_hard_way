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

class scenarios(object):
    pass


class Tunnel(scenarios):

    def enter(self):
        print("You are in Room 'tunnel'")
        exit()

class firstRoom(scenarios):
    def enter(self):
        print("You are in Room:'first room'")
        exit()

class Pit(scenarios):
    def enter(self):
        print("You are in Room:'pit'")
        exit()
    
class DiamondRoom(scenarios):
    def enter(self):
        print("You are in Room:'diamondroom'")
        exit()

class DarkTunnel(scenarios):
    def enter(self):
        print("You are in Room:'darktunnel'")
        exit()

class Pool(scenarios):
    def enter(self):
        print("You are in Room:'pool'")
        exit()

class Arena(scenarios):
    def enter(self):
        player.select_weapon()
        print("You are in Room:'arena'")
        exit()

class Staircase(scenarios):
    def enter(self):
        print("You are in Room:'staircase'")
        exit()

class Engine(object):
    def play(next_scenario):
        pass

class Router(object):

    rooms={
        "tunnel": tunnel(),
        "first room": tunnel(),
        "pit": tunnel(),
        "diamond room": tunnel(),
        "dark dunnel": tunnel(),
        "pool": tunnel(),
        "arena": tunnel(),
        "staircase": tunnel()
    }

    def __init__(self, start_scenario):

        self.start_scenario = start_scenario
    
    def next_scenario():
        
        print("test")
        self.rooms.get(self.start_scenario)


#Other funtions


#Debug and test funtions


#Main
player = Player(input("Hello Advanturer, whats your Name?\n-->"))
print("Welcome",player.name)
player.select_tool()
#
#
start = Router("tunnel")
start.next_scenario()


