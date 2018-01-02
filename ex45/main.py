from sys import exit
import scenarios
# from characters import Character

class Engine(object):

    def __init__ (self, room):
        self.room = room


    def play(self):
        current_room = self.room.next_scenario(self.room.start_scenario)
        last_room = self.room.next_scenario("staircase")

        while current_room != last_room:
            var = current_room.enter()
            current_room = self.room.next_scenario(var)
        
        last_room.enter()

class Router(object):

    rooms={
        "main menu": scenarios.MainMenu(),
        "death": scenarios.Death(),
        "tunnel": scenarios.Tunnel(),
        "behind door": scenarios.BehindDoor(),
        "pit": scenarios.Pit(),
        "diamond room": scenarios.DiamondRoom(),
        "dark dunnel": scenarios.DarkTunnel(),
        "pool": scenarios.Pool(),
        "arena": scenarios.Arena(),
        "staircase": scenarios.Staircase()
    }

    def __init__(self, start_scenario):

        self.start_scenario = start_scenario
    
    def next_scenario(self, scenario):
         val = self.rooms.get(scenario)
         return val

#Main
a_router = Router("main menu")
a_engine = Engine(a_router)


a_engine.play()