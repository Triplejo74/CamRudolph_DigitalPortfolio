# Main game file
import os
import random
import pickle as p
import Characters as c

dis = 100
mSlain = 0
coin = 0
inventory = { "Gold": 100, "Potions": 5, "Monster Parts": 5 }
hPause = 0

town = 0
tVis = 0
hUP = 0
dUP = 0

sCave = 0

# The user is prompted on if they want to play the game. If they put "y" the game will start.
while coin == 0:
    ply = input("""Adventurer's Rush

Do you wish to play Adventurer's Rush?
y = Yes
n = No \n""")

    if ply == "y":
        while town == 0: # The user is given the option to enter the town to upgrade equipment, buy potions, or sell monster parts
            dis = 100

            #The first prompt of for the user of where to go
            peanut = input("""Your Adventure awaits!
What will you do?
t = Go into town
c = Go into the Caves \n""")
            if peanut == "t":
                while tVis == 0:

                    #Town prompt giving the player options to better their hero 
                    shop = input("""You enter the town and notice a few shops. Where do you go?
b = Blacksmith (Upgrade armor)
t = Trainer (Train with a trainer)
a = Alchemist (Buy more potions)
m = Monster Guild (Sell your monster parts)
i = Inventory (Check your inventory)
l = Leave (Go into the cave)
q = Quit (Quit the Game)\n""")
                    
                    #Blacksmith adds more HP to the player's total health for the price of 50 gold
                    if shop == "b":
                        bAns = input("Would you like to upgrade your armor for 50 gold giving you +5 HP? (y = Yes, n = No)\n")
                        if bAns == "y":
                            if inventory["Gold"] - 50 >= 0:
                                inventory["Gold"] -= 50
                                hUP += 5
                                c.player.maxHealth = c.player.health + hUP
                                print("Remaining Gold: ", inventory["Gold"])
                                print("New HP: ", c.player.health + hUP, '/', 80 + hUP)
                            else:
                                input("You do not have enough gold.\nPress \"Enter\" to continue")

                    #Trainer adds two more damage automatically before the damaged is rolled. Training is 30 gold
                    if shop == "t":
                        tAns = input("Would you like to train with a master to improve your damage by 2 for 30 Gold? (y = Yes, n = No)\n")
                        if tAns == "y":
                            if inventory["Gold"] - 30 >= 0:
                                inventory["Gold"] -= 30
                                dUP += 2
                                print("Remaining Gold: ", inventory["Gold"])
                                print("New Damage: ", c.player.power + dUP)
                            else:
                                input("You do not have enough gold.\nPress \"Enter\" to continue")

                    #Alchemist adds another potion to the inventory for the price of 20 gold
                    if shop == "a":
                        aAns = input("Would you like to go into the Alchemist's shop and buy a potion for 20 gold? (y = Yes, n = No)\n")
                        if aAns == "y":
                            if inventory["Gold"] - 20 >= 0:
                                inventory["Gold"] -= 20
                                inventory["Potions"] += 1
                                print("Remaining Gold: ", inventory["Gold"])
                                print("Potions: ", inventory["Potions"])
                            else:
                                input("You do not have enough gold.\nPress \"Enter\" to continue")

                    #Moster guild allows the player to sell the Monster parts they gathered in the cave for 10 gold a piece
                    if shop == "m":
                        mAns = input("Would you like to sell your monster parts for 10 Gold a piece? (y = Yes, n = No)\n")
                        if mAns == "y":
                            if inventory["Monster Parts"] > 0:
                                mShop = inventory["Monster Parts"] * 10
                                inventory["Monster Parts"] = 0
                                inventory["Gold"] += mShop
                                print("Total Gold: ", inventory["Gold"])
                            else:
                                input("You do not have any Monster Parts to sell.\nPress \"Enter\" to continue")

                    #Inventory displays the players gold, potions, and monster parts. It also displays the player's health and damage range
                    if shop == "i":
                        print(inventory)
                        print("Current HP: ", c.player.health + hUP)
                        print("Current Damage: ", c.player.power + dUP)
                        iPau = input("Press \"Enter\" to continue\n")
                    if shop == "l":
                        lAns = input("Would you like to leave the town and enter the caves? (y = Yes, n = No)\n")
                        if lAns == "y":
                            peanut = "c"
                            break
                        else:
                            input("You decide to stay in town.\nPress \"Enter\" to continue")

                    #Quit quits and closes out the game
                    if shop == "q":
                        input("The Adventurer left the game. Press Space to close")
                        quit()

            #Puts the player into the caves using random number chances to encounter an enemy
            if peanut == "c":
                mSlain = 0
                while dis >= 1:
                    encounterChance = random.randrange(10)
                    if encounterChance <= 3: 
                        opponent = random.choice(c.monsterList)
                        print("\nA " + opponent.name + " appears and attacks.", encounterChance) 
                        while c.player.health > 0 and opponent.health > 0:      #The battle phase using each characters HP and damage to attack hurt each other     
                            c.player.fight(opponent)                            #the Fight function has a random number pulled from the characters damage range
                            opponent.fight(c.player)
                            print("Current health: " + str(c.player.health + hUP))
                            print("Opponents health: " + str(opponent.health - dUP) + "\n")
                            btl = input("What will you do? (f = Fight, r = Runaway) ")

                             #Player could also run setting them back by 15
                            if btl == "r":
                                print("You run away but your progress to leave the cave is set back.")
                                dis += 15
                                rPau = input("Press \"Enter\" to continue \n")
                                break

                            #Once the opponent is defeated, the player is given monster parts based on the opponent they fought
                            if opponent.health - dUP <= 0:
                                print("You slayed the " + opponent.name)
                                mSlain += 1
                                mPrt = random.randrange(opponent.loot)
                                print("You loot " + str(mPrt) + " parts from the " + opponent.name + " and put them in your inventory.")
                                inventory["Monster Parts"] += mPrt
                                kPau = input("Press \"Enter\" to continue \n")
                                opponent.health 
                                opponent.health = opponent.maxHealth
                                break

                        #If the player's HP goes to or below zero the game ends
                        if c.player.health + hUP <= 0:
                            input("You were slain by a monster and defeated " + str(mSlain) + " monsters. Press \"Enter\" to quit.")
                            quit()

                    #The player's movement is tracked and is prompted on what to do
                    print("Meters from escaping the cave " + str(dis))
                    dis -= random.randrange(1, 20)
                    Ans = input("What will you do?(c = Continue, g = Give up, h = Heal, i = Inventory) \n")

                    #During the cave the player can quit out inbetween movement and battling
                    if Ans == "g":
                        giveUp = input("Are you sure you want to give up? (\"y\" = yes or \"n\" = no)\n")
                        if giveUp == "y":
                            input("The Adventurer gave up and was lost to the cave.")
                            quit()
                        input("Continuing on. (Press \"Enter\" to continue)")

                    #The player can choose to heal while in the cave
                    if Ans == "h":
                        while hPause == 0:
                            hAns = input("Would you like to use a potion? (y = Yes, n = No) \n")
                            if hAns == "y":
                                if inventory["Potions"] > 0:            #The player is prompted to use a potion, If they do it will
                                    inventory["Potions"] -= 1           #subtract one from their total potion pool and add 25 HP back.
                                    if c.player.health <= 79 + hUP:     #If the player is at or above max health it will have no effect
                                        c.player.health += 25
                                        print("Number of potions left: ", inventory["Potions"])
                                        print("Current HP: ", c.player.health + hUP, "/", 80 + hUP)
                                    else:
                                        print("The potion has no effect (HP at Max)" + "\nCurrent HP: ", c.player.health + hUP)
                                        hMax = input("Press \"Enter\" to continue \n")
                                        break
                                else:
                                    print("You look through bag and find no potions to use") 
                                    nPot = input("Press \"Enter\" to continue \n")
                                    break
                            else:
                                break

                    #The player checks their inventory and displays their current health too 
                    if Ans == "i":
                        print(inventory, "\nCurrent HP: ", c.player.health + hUP)
                        iPau = input("Press \"Enter\" to continue\n")

                    #Save game function that is not quite working as intended. Taken out until fixed
                    '''if Ans == "s":
                        save_dir = os.path.join("Adventures_Rush", "Saved_Game")
                        if not os.path.exists(save_dir):
                            os.makedirs(save_dir)
                        with open(os.path.join(save_dir, "distance.pk1"), "wb") as dFile:
                            p.dump(dis, dFile)
                        with open(os.path.join(save_dir, "health.pk1"), "wb") as hFile:
                            p.dump(c.player.health, hFile)
                        with open(os.path.join(save_dir, "MonsterSlain.pk1"), "wb") as mFile:
                            p.dump(mSlain, mFile)
                        with open(os.path.join(save_dir, "inventory.pk1"), "wb") as iFile:
                            p.dump(inventory, iFile)
                        sPau = input("Game Saved!\nWould you like to quit? (y = Yes, n = No)\n")
                        if sPau == "y":
                            print("The Adventurer left the game.")
                            quit()
                        else:
                            print("You continue your adventure.")'''

                #After successfully completing a run the monsters they slain will display and the player goes back to full HP
                print("You've left the caves after defeating ", mSlain, " monsters and rest in town!")
                c.player.health = c.player.maxHealth
        town = 1

        #Load Game function that is not working. Doing more research into progress saving
    '''if ply == "o":
        try:
            save_dir = os.path.join("Adventures_Rush", "Saved_Game")
            c.player.load_distance(os.path.join(save_dir, "distance.pk1"))
            c.player.load_MonsterSlain(os.path.join(save_dir, "MonsterSlain.pk1"))
            c.player.load_inventory(os.path.join(save_dir, "inventory.pk1"))
            c.player.load_health(os.path.join(save_dir, "health.pk1"))
            town = 1
            print("Saved Game Loaded")
            ply = input("Would you like to continue? (y = Yes, n = No)\n")
            if ply == "y":
                print("Continuing your adventure...")
            else:
                print("The Adventurer left the game.")
                quit()
        except FileNotFoundError:
            print("No saved game file found.")'''

    #If the player chooses to not play it will quit the program. 
    if ply == "n":
        quit()
