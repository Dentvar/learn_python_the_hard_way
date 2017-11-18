import sys
script, counter, jumps = sys.argv
#Funcions
def create_list_while(counter, jumps):
    i = 0
    numbers = []
    while i < counter:
        numbers.append(i)
        print(f"Numbers now: {numbers}")
        i += jumps
    return numbers

def create_list_for(counter,to):
    numbers = []
    for i in range(counter,to):
        numbers.append(i)
        print(f"Number now: {numbers}")
    return numbers


####################################################


#Variable defenitions
counter = int(counter)
jumps = int(jumps)
####################################################


#Main
numbers = create_list_for(counter, jumps)

####################################################