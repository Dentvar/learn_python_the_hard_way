import fileinput

def clear_file(file):
    # Just deletes the content of the file. For testing only.
    f = open(file, "w")
    f.write("")
    f.close

def convert_file_to_list(file, player_name):
    """converts the given file into a list and returns it"""
    f = open(file, "r")
    l = []
    for line in f:
        s = line.strip("\n")
        s = s.split(",")

        l.append(s)
    
    f.close()
    return (l)


def save_highscore(l, file): 

    new_player = False



    for i in l:
        if i[0] == player_name:

            n = int(i[1])
            search = str(n)
            n += 1
            print("printing 'n' as Integer", n)
            n_string = str(n)
            print("printing 'n' as String", n)
            # print("Highscore of current Player updated")
            f = open(file, "w")
            for line in f:
                line.replace(search, n_string) # würde jede gefundene Zahl ersetzen nicht nur da wo Player_name übereinstimmt.
            f.close()
            new_player = False
            break

        else:
            new_player = True

    if new_player:
        print("Your are a new player")
        f = open(file, "a")
        f.write(player_name +"," + player_tries + "\n")
        print("Highscore for current Player Created")
        f.close()
    else:
        pass

def load_last_player_data(l):
# search for player name in the file and if found load its number of tries

    val = "0"
    for i in l:
        if i[0] == player_name:
            val = i[1]
            break
        else:
            val = "1"

    return val

f = "./Highscore_list.txt"
player_name = input("Whats your name\n-->")
highscore_list = convert_file_to_list(f, player_name)
player_tries = load_last_player_data(highscore_list)
print("Player tries just after loading", player_tries)
save_highscore(highscore_list, f)
print("Player tries after saving", player_tries)




















# test = highscore_list.read()
# print(test)

# test = highscore_list.readline()
# print(test)

# test = highscore_list.readlines()
# print(test)

# test = ["Monday", "Dienstag", "Mittwoch", "Donerstag", "Freitag", "Samstag", "Sonntag"]
# for i in test:
#     string = "\n" + i
#     highscore_list.write(string)
#     highscore_list.write("\n")
# print("done")

# highscore_list.write(Column1 +"," + Column2+ "\n")

# save_highscore()
