# Main game file
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
n = No
o = Open saved file \n""")
    if ply == "y":
        while town == 0: # The user is given the option to enter the town to upgrade equipment, buy potions, or sell monster parts
            dis = 100
            peanut = input("""Your Adventure awaits!
What will you do?
t = Go into town
c = Go into the Caves \n""")
            if peanut == "t":
                while tVis == 0:
                    shop = input("""You enter the town and notice a few shops. Where do you go?
b = Blacksmith (Upgrade armor)
t = Trainer (Train with a trainer)
a = Alchemist (Buy more potions)
m = Monster Guild (Sell your monster parts)
l = Leave (Go into the cave)\n""")
                    if shop == "b":
                        bAns = input("Would you like to upgrade your armor for 50 gold giving you +5 HP? (y = Yes, n = No)\n")
                        if bAns == "y":
                            if inventory["Gold"] - 50 >= 0:
                                inventory["Gold"] -= 50
                                hUP += 5
                                print("Remaining Gold: ", inventory["Gold"])
                                print("New HP: ", c.player.health + hUP)
                            else:
                                input("You do not have enough gold.\nPress \"Enter\" to continue")
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
                    if shop == "a":
                        aAns = input("Would you like to go into the Alchemist's shop and buy a potion? (y = Yes, n = No)\n")
                        if aAns == "y":
                            if inventory["Gold"] - 20 >= 0:
                                inventory["Gold"] -= 20
                                inventory["Potions"] += 1
                                print("Remaining Gold: ", inventory["Gold"])
                                print("Potions: ", inventory["Potions"])
                            else:
                                input("You do not have enough gold.\nPress \"Enter\" to continue")
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
                    if shop == "l":
                        lAns = input("Would you like to leave the town and enter the caves?\n")
                        if lAns == "y":
                            peanut = "c"
                            break
                        else:
                            input("You decide to stay in town.\nPress \"Enter\" to continue")
            if peanut == "c":
                while dis >= 1:
                    encounterChance = random.randrange(10)
                    if encounterChance < 4: 
                        opponent = random.choice(c.monsterList)
                        print("\nA " + opponent.name + " jumps out and attacks.")
                        while c.player.health > 0 and opponent.health > 0:
                            c.player.fight(opponent)
                            opponent.fight(c.player)
                            print("Current health: " + str(c.player.health + hUP))
                            print("Opponents health: " + str(opponent.health - dUP) + "\n")
                            btl = input("What will you do? (f = Fight, r = Runaway) ")
                            if btl == "r":
                                print("You run away but your progress to leave the cave is set back.")
                                dis += 15
                                rPau = input("Press \"Enter\" to continue \n")
                                break
                            if opponent.health - dUP <= 0:
                                print("You slayed the " + opponent.name)
                                mSlain += 1
                                mPrt = random.randrange(0, 8)
                                print("You loot " + str(mPrt) + " parts from the " + opponent.name + " and put them in your inventory")
                                inventory["Monster Parts"] += mPrt
                                kPau = input("Press \"Enter\" to continue \n")
                                break
                        if c.player.health + hUP <= 0:
                            print("You were slain by a monster and defeated " + str(mSlain) + " monsters.")
                            quit()

                    print("Meters from escaping the cave " + str(dis))
                    dis -= random.randrange(1, 20)
                    Ans = input("What will you do?(c = Continue, g = Give up, h = Heal, i = Inventory, s = Save game) \n")
                    if Ans == "g":
                        print("The Adventurer gave up and was lost to the cave.")
                        quit()
                    if Ans == "h":
                        while hPause == 0:
                            hAns = input("Would you like to use a potion? (y = Yes, n = No) \n")
                            if hAns == "y":
                                if inventory["Potions"] > 0:
                                    inventory["Potions"] -= 1
                                    if c.player.health <= 79 + hUP:
                                        c.player.health += 25
                                        print("Number of potions left: ", inventory["Potions"])
                                        print("Current HP: ", c.player.health + hUP)
                                    else:
                                        print("The potion has no effect (HP at Max)")
                                        hMax = input("Press \"Enter\" to continue \n")
                                        break
                                else:
                                    print("You look through bag and find no potions to use")
                                    nPot = input("Press \"Enter\" to continue \n")
                                    break
                            else:
                                break
                    if Ans == "i":
                        print(inventory)
                        iPau = input("Press \"Enter\" to continue\n")
                    if Ans == "s":
                        with open("distance.pk1", "wb") as dFile:
                            p.dump(dis, dFile)
                        with open("health.pk1", "wb") as hFile:
                            p.dump(c.player.health, hFile)
                        with open("MonsterSlain.pk1", "wb") as mFile:
                            p.dump(mSlain, mFile)
                        with open("inventory.pk1", "wb") as iFile:
                            p.dump(inventory, iFile)
                        sPau = input("Game Saved!\nPress \"Enter\" to continue\n")

                print("You've left the caves after defeating ", mSlain, " monsters!")
                coin = 1
                quit()
        town = 1
    if ply == "o":
        try:
            with open("distance.pk1", "rb") as dFile:
                dis = p.load(dFile)
            with open("MonsterSlain.pk1", "rb") as mFile:
                mSlain = p.load(mFile)
            with open("inventory.pk1", "rb") as iFile:
                inventory = p.load(iFile)
            c.player.load_health("health.pk1")
            coin = 1
            print("Saved Game Loaded")
        except FileNotFoundError:
            print("No saved game file found.")
    if ply == "n":
        quit()
