import characters
characters = characters.Character()
from textwrap import dedent

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
        print(dedent("""
        -----------------------------------------------------------------------------------
        You are in a barren dessert and decided to dig for some old ruins around this area.
        You researches have shown that there are a lot of hidden tressures in this zone.
        You start to dig down creating a tunnel. Suddenly you find a big door
        What will be behind it?!
        But how to open it...
        There is a riddel writen on it. Maybe speaking out loud the answer will open it?
        """))

        print("The ridel is:\nWhat's strong enough to smash ships but still fears the sun?\n")

        print("Whats your answer?")
        print("1. Fire")
        print("2. Ice")
        print("3. Earth")
        print("4. Air")
        
        answer = str.lower(input("-->"))

        if answer == "1" or answer == "fire":

            print("Wrong!")
            print("A small hole in the rocks opens and fire bursts out... burning you to death.")

            return("death")

        if answer == "2" or answer == "ice":
            
            print("Correct!")
            print("You hear a 'click' and the door opens.")
            print("Behind the door there is a small corridor.")
            print("You step into the corridor")
            print("As soon as you steped in, the door closes again")

            return "behind door"

        if answer == "3" or answer == "earth":

            print("Wrong!")
            print("The walls rumble and start moving to each other. Killing you between them")

            return("death")
        if answer == "4" or answer == "air":

            print("Wrong!")
            print("You hear a sound... its gas filling the room. You die a horrible death breathing it.")

            return("death")

class BehindDoor(Scenarios):
    def enter(self):
        print(dedent("""
        It's completly dark in the room. Only on the other side,
        there is a small glimmering light. It seems like the way has been blocked by rocks.
        """))
        if player.tool == "lighter":
            print(dedent("""Luckyly you picked the lighter with you. Before going towards the light,))
        

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