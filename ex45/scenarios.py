import characters
characters = characters.Character()

from textwrap import dedent
from random import randint

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
        #Cheat code
        elif selection =="gato":
            print("Cheater!!!")
            player.tool = "rope"
            return(str.lower(input("Input the room you want to go to\n-->")))
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
            print(dedent("""
            Luckyly you picked the lighter with you.
            Before going towards the light, you make a torch out of the shovel stick
            and a bit of cloth that you were.
            Nearly you would have missed the big hole in the floor. You go around it
            and reach the rocks that are blocking the way to the next room
            """))
            return ("diamond room")
        else:
            print(dedent("""
            You start going toward the light. Suddenly you lose the ground under your feet. You notice how you fall down...
            """))
            return("pit")
        

class Pit(Scenarios):
    def enter(self):
        print(dedent("""
        You felt into a Pit.
        You look around, it seems as its just some meter high.
        """))

        if player.tool == "rope":
            print(dedent("""
            You take the rope and makes a knot on one side and throw it up.
            Somehow you manage to get it stuck on something and climbs out the hole
            Finally you reach the next room with the strange light.
            The rope however was damaged by friction and is useless now.
            """))
            #could set player.tool to "none" but for now nothing would use this state.
            return ("diamond room")
        else:
            print(dedent("""
            There seems to be no way out here, you try for days to climb out of the hole.
            The bottle of water you took with you is slowly running out of water and finnaly you die there.
            """))
            return ("death")
        exit()
    
class DiamondRoom(Scenarios):
    def enter(self):
        print(dedent("""
        Once you reached the room with the strange light, you see that the light comes from...
        A huge diamond that is on a pedestal in the middel of the room.
        
        In the seeling there is a hole and the sun is shining in, pointing direkctly on the diamond that makes the room shine like there was a disco bole.
        You look around, the room it's shaped as a pentagon and there are 4 doors going out. Including the one you just came from.
        You goes near the diamond. It does not seem to be fixed in anyway on the pedestal. No mecanism or trap seems visible.
        Strange...

        So finally you decide to carefully take it down.
        But you were wrong. Once you completly took of the weight of the pedestal a "click" sounds and a deep rumbling goes throght the dungeon.
        Suddenly the sealing of the room, that you just have come from falls down and the way is blocked.

        So now you only can choose between 3 doors.
        You do not know what is behind each of this doors.
        There are no marks or hinds what could be behind this doors. So you need to decide for one of them.
        """))

        return(self.random_room_asignation())
        #makes sure that rooms are not the same in each playthough.

    def random_room_asignation(self):
        
        #Random Asignation of a,b,c
        a = randint(0, 2)

        b = randint(0, 2)
        while b == a:
            b = randint(0, 2)

        c = randint(0, 2)
        while c == a or c == b:
            c = randint(0, 2)

        tup=(
            "dark tunnel",
            "pool",
            "arena"
            )

        door =  str.lower(input("-->"))

        if door == "1":
            return(tup[a])
        elif door == "2":
            return(tup[b])
        elif door == "3":
            return(tup[c])
        else:
            print("Does not compute")
            return ("diamond room")


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