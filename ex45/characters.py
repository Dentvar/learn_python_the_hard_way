class Character(object):


    tools={
        "lighter",
        "rope",
        "bottle of water"
    }

    weapons={
        "sword",
        "crossbow",
        "shield",
        "spear"
    }

    
    def counter(self):
        self.attamps = 0
        # open(savedata.txt, w)
        self.attamps += 1
        print("Counter is now:", self.attamps)


    def character_creations(self):
        self.name = input("Hello Advanturer, whats your Name?\n-->")

        savedata = open("savedata.txt", "w")
        for line in savedata:
            readed_value = savedata.readline()
            if readed_value == self.name:
                val = 0
            else:
                val = 1
            
        if val == 1:
            print("Val is 1")
            # self.name hinzufügen
            # count dazu auf 0 setzen
        else:
            print("Val is 0")
            # denn zu gehörigen count suchen
        # close(savedata)

        print("Welcome",self.name)

    def select_tool(self):
        print("You can choose one of the following items for your Advanture:")
        print("\nPossible tools:")
        # List the items of the tools list
        for i in self.tools:
            print("-", i)

        print("What tool do you want?\n-->")
        self.tool = str.lower(input())

        # check if input is correct
        if self.tool != "lighter" and self.tool != "rope" and self.tool != "bottle of water":
            print("Does not compute. Try again")
            self.select_tool()
        else:
            # if input is correct just go on.
            print(f"You have choosen {self.tool} as a tool.")

    def select_weapon(self):
        print("You can choose one of the following Weapons:")
        print("\nPossible Weapons:")

        # List the items of the weapons list
        for i in self.weapons:
            print("-", i)

        print("What Weapon do you choose?\n-->")
        self.weapon = str.lower(input())

        # check if input is correct
        if self.weapon != "sword" and self.weapon != "crossbow" and self.weapon != "shield" and self.weapon != "spear":
            print("Does not compute. Try again")
            self.select_weapon()
        else:
            # if input is correct just go on.
            print(f"You have choosen {self.weapon} as tool.")           

