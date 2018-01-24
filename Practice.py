from random import randint


a = randint(0, 2)

b = randint(0, 2)
while b == a:
    b = randint(0, 2)

c = randint(0, 2)
while c == a or c == b:
    c = randint(0, 2)

print("a is:", a)
print("b is:", b)
print("c is:", c)

tup=(
    "dark tunnel",
    "pool",
    "arena"
    )

door =  str.lower(input("-->"))

print ("tub[a] is:", tup[a])
print ("tub[b] is:", tup[b])
print ("tub[c] is:", tup[c])

if door == "1":
    print(tup[a])
if door == "2":
    print(tup[b])
if door == "3":
    print(tup[c])