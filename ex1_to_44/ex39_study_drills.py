#This are teh study Drills for "Learn Pyhton the hard way" Ex39.

#All countries that are available

selected_countrie = 0
i = 0

def count_values_in_dic(dic_name):
    count = int(0)
    for x, y in dic_name.items():
        count += (len(dic_name[x]))
    return count

def countrie_selection(countrie):
    
    global selected_countrie

    if countrie == "Germany" or countrie == "DE":
        selected_countrie = "DE"
        print(f"The following states are in {countrie}:\n")
        
    elif countrie == "Spain" or countrie == "ES":
        selected_countrie = "ES"
        print(f"The following states are in {countrie}:\n")
        
    elif countrie == "Italy" or countrie == "IT":
        selected_countrie = "IT"
        print(f"The following states are in {countrie}:\n")

    else:
        print("Please enter on of the avaiable countries. Either by it's full name or its abbretive 'DE', ES, 'IT'")
        countrie_selection(input("> "))

def list_states(countrie):
    
    i = 0
    for x in states[countrie]:
        i = i + 1
        print (f"{i}.", x)

def list_cities(state):
    city = cities.get(state)
    if city == None:
        print("Not a valid State, please try again")
        list_cities(input("> "))
    else:
        print(city)
        again()

def again():
    next_state = input("Do you want to know about a other city? 'Y/N'")
    if next_state == "Y" or next_state =="Yes":
        list_cities(input("> "))
    elif next_state == "N" or next_state =="No":
        print("See you next time")
        exit()
    else:
        print("Please type in:\n 'Y' for Yes\n'N' for No")
        again()
    
    


#List of all supported countries
countries = {
    "Germany": "DE",
    "Spain": "ES",
    "Italy": "IT"
}

#States in each countrie
states = {
    "DE": {"Baden-Württenberg", "Bayern", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"},
    "ES": {"Andalucia", "Aragon", "Cantabria", "Castilla y Leon", "Castilla-La Mancha", "Cataluña", "Ceuta", "Madrid", "Valencia", "Extremadura", "Galicia", "Illes Baleares", "Islas Canarias", "La Rioja", "Melilla", "Navarra", "Pais Vasco", "Asturias", "Murcia"},
    "IT": {"Lombardei", "Kampanien", "Latium", "Sizilien", "Venetien", "Piemont", "Emilia-Romagna", "Apulien", "Toskana", "Kalabrien", "Sardinien", "Ligurien", "Marken", "Abruzzen", "Friaul-Julisch Venetien", "Trentino-Südtirol", "Umbrien", "Basilikata", "Molise", "Aostatal"}
}

#Main city for eache State
cities = {
    "Baden-Württenberg": "Stuttgart",
    "Bayern": "München",
    "Berlin": "Berlin",
    "Brandenburg": "Potsdam",
    "Bremen": "Bremen",
    "Hamburg": "Hamburg",
    "Hessen": "Wiesbaden",
    "Mecklenburg-Vorpommern": "Schwerin",
    "Niedersachsen": "Hannover",
    "Nordrhein-Westfalen": "Düsseldorf",
    "Rheinland-Pfalz": "Mainz",
    "Saarland": "Saarbrücken",
    "Sachsen": "Dresden",
    "Sachsen-Anhalt": "Magdeburg",
    "Schleswig-Holstein": "Kiel",
    "Thüringen": "Erfurt",
    "Andalucia": "Sevilla",
    "Aragon": "Zaragoza",
    "Cantabria": "Santander",
    "Castilla y Leon": "Valladolid",
    "Castilla-La Mancha": "Toledo",
    "Cataluña": "Barcelona",
    "Ceuta": "Cueta",
    "Madrid": "Madrid",
    "Valencia": "Valencia",
    "Extremadura": "Merida",
    "Galicia": "Santiago de Compostela",
    "Illes Baleares": "Palma de Mallorca",
    "Islas Canarias": "Las Palmas de Gran Canaria",
    "La Rioja": "Logroño",
    "Melilla": "Melilla",
    "Navarra": "Pamplona",
    "Pais Vasco": "Victoria",
    "Asturias": "Oviedo",
    "Murcia": "Murcia",
    "Lombardei": "Milano",
    "Kampanien": "Napoli",
    "Latium": "Roma",
    "Sizilien": "Palermo",
    "Venetien": "Venezia",
    "Piemont": "Torino",
    "Emilia-Romagna": "Bologna",
    "Apulien": "Bari",
    "Toskana": "Firenze",
    "Kalabrien": "Catanzaro",
    "Sardinien": "Cagliari",
    "Ligurien": "Genova",
    "Marken": "Ancona",
    "Abruzzen": "L'Aquila",
    "Friaul-Julisch Venetien": "Trieste",
    "Trentino-Südtirol": "Trentino",
    "Umbrien": "Perugia",
    "Basilikata": "Potenza",
    "Molise": "Campobasso",
    "Aostatal": "Aosta",
}

#Main

print("This programm can tell you about all Reagions and their main cities of the following countries:\n")

#list available countries
for x, y in countries.items(): 
    i = i + 1
    print(f"{i}.{x} - {y}")

countrie_selection(input("\nSelect the countrie you wish to see the info about:\n> "))
list_states(selected_countrie)
list_cities(input("You can now choose one state in order to show its main city.\n> "))


#Idea of the Program
# Ideas what my programm should do:
# -Let user make a choice of wich country to choose by abbrev or full name
# Based on the choice, list all states
#User select one state and programm will list all cities
#Ask if he wants to know abut a other countrie or State.

#To Do's
# Get the lists/dics from a file instead of manually tiping it in here. (Maybe Web-scrabble?)
#DO all this with a very simple GUI
#in order to import from file a list see oop_test.py