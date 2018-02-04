name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

def to_kg(int):
    weight/2.20462
def to_cm(int):
    a = height*2.54

print(f"lets see if this works call to_kg {to_kg(weight)}.")
print(f"let's talk about {name}.")
print(f"He's {int(height*2.54)} cm/ {height} inches tall.")
print(f"He's {int(weight/2.20462)} kg/ {weight} lbs heavy.")
print("Actually taht's not to heavy.")
print(f"he's got {eyes} eyes and {hair} hjair.")
print(f"His teeth are usually {teeth} dcepending on the cofee.")

total = age + height + weight
print(f"If I add {age},{height}, and {weight} I get {total}.")