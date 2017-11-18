the_count = [1, 2, 3, 4, 5,]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this first kind of for-loop goes throught a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go throgh mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
#not necesarry we initialize the list bellow in line 24 anyway.
elements = []

#then use the range focunion to do 0 to 5 counts

elements = range(0,6)
elements2 = elements[:]
#now we can print them out too
for i in elements:
    print(f"Element was: {i}")

for i in elements2:
    print (elements2[i])

print (f"What is i now?: {i}")