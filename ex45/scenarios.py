import characters
characters = characters.Character()

# Define Player as global and instance of Character()
global player
player = characters

class Scenarios(object):
    # Only because it seems I need a parent for the other rooms
    pass

class MainMenu(Scenarios):

    def enter(self):
        print("Welcome to the game.")
        print("What do you wan't to do?")
        print("1. Play")
        print("2. Exit")
        selection = str.lower(input("-->"))

        if selection == "1" or selection == "play":
            player.character_creations()
            player.select_tool()
            return "tunnel"
        elif selection == "2" or selection == "exit":
            exit()
        else:
            print("Does not compute")
            return "main menu"

class Death(Scenarios):

    def enter(self):
        print("You died...")
        print("Game Over!")
        print("Do you want to try again?")
        print("1. Yes")
        print("2. No")
        selection = str.lower(input("-->"))


        if selection == "1" or selection == "yes":
            # Maybe reset some variables?! WIP
            return "tunnel"
            
        elif selection == "2" or selection == "no":
            # Maybe save some variables once save games are included! WIP
            return "main menu"
        else:
            print("Does not compute")
            return("death")

class Tunnel(Scenarios):

    def enter(self):
        print("You are in Room 'tunnel'")
        if player.tool == "rope":
            pass
        else:
            pass
        exit()

class BehindDoor(Scenarios):
    def enter(self):
        print("You are in Room:'Behind Door'")
        exit()

class Pit(Scenarios):
    def enter(self):
        print("You are in Room:'pit'")
        exit()
    
class DiamondRoom(Scenarios):
    def enter(self):
        print("You are in Room:'diamondroom'")
        exit()

class DarkTunnel(Scenarios):
    def enter(self):
        print("You are in Room:'darktunnel'")
        exit()

class Pool(Scenarios):
    def enter(self):
        print("You are in Room:'pool'")
        exit()

class Arena(Scenarios):
    def enter(self):
        player.select_weapon()
        print("You are in Room:'arena'")
        exit()

class Staircase(Scenarios):
    def enter(self):
        print("You are in Room:'staircase'")
        exit()