
f = "./Highscore_list.txt"
highscore_list = open(f, "r")

def clear_file():
    highscore_list.write("")

def save_highscore():
    highscore_list.write(player_name +"," + player_tries + "\n")
    print("Highscore of current Player saved")

def load_last_player_data():
    for i, line in enumerate(highscore_list):
        test = highscore_list.readline()
        if test == player_name + "," + player_tries:
            print("found")
        else:
            print(str(test) + str(i))
            print("not found")

Column1 = "Player Name"
Column2 = "Player Tries"
player_name = "Svadun"
player_tries = "80"

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
load_last_player_data()
highscore_list.close