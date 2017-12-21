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

# Room functions:

def tunnel():
    print("You are in Room 'tunnel'")
    first_room()

def first_room():
    print("You are in Room:'first room'")
    death()

def pit():
    print("You are in Room:'pit'")
    exit()
    
def diamond_room():
    print("You are in Room:'diamond_room'")
    exit()

    
def dark_tunnel():
    print("You are in Room:'dark_tunnel'")
    exit()

    
def pool():
    print("You are in Room:'pool'")
    exit()

    
def arena():
    print("You are in Room:'arena'")
    exit()
    
def staircase():
    print("You are in Room:'Staircase'")
    exit()

def dead():
    print("You are in Room:'dead'")
    again = str.lower(Input("Do you wan't to try again?"))
    if again == "yes" or again == "y":
        player.select_tool()
        tunnel()
    elif again == "yes" or again == "y":
        print("Thank's for playing")
        exit()
    else:
        print("Does not compute")
        dead()


#Other funtions

#Debug and test funtions


#Main
player = Player(input("Hello Advanturer, whats your Name?\n-->"))
print("Welcome",player.name)
player.select_tool()
tunnel()