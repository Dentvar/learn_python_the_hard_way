import fileinput

def clear_file(file):
    """Just deletes the content of the file. For testing only."""
    f = open(file, "w")
    f.write("")
    f.close

def get_last_player_score(file, player_name):
    """searches for player name and gives back his lasts score"""
    f = open(file, "r")
    for line in f:
        string = line.split(",")
        if string[0] == player_name:
            score = int(string[1].strip("\n"))
            break
        else:
            score = 0
    f.close()

    if score > 0:
        print("Welcome Back", player_name, "you have played",score, "times")
    else:
        print("new Player")

    return (score)

def save_highscore(l, file): #unfinished

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


f = "./Highscore_list.txt"
player_name = input("Whats your name\n-->")

# highscore_list = convert_file_to_list(f)
# player_tries = load_last_player_data(highscore_list)
# save_highscore(highscore_list, f)

get_last_player_score(f, player_name)



















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
