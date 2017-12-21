from sys import exit

def test():
    print("soy test")
    exit()

scenes = {
    'central_corridor': "CentralCorridor()",
    'laser_weapon_armory': "LaserWeaponArmory()",
    'the_bridge': "TheBridge()",
    'escape_pod': "EscapePod()",
    'death': test,
    'finished': "Finished()",
    }

print(scenes.get("death"))
scenes.get("death")()