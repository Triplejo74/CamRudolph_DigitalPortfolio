# Characters.py
import random
import os
import pickle as p

class GameCharacter:
    #Character Object that has name, power, health, max health, and how much loot they can have
    def __init__(self, name, power, health, maxHealth, loot):
        self.name = name
        self.power = power
        self.health = health
        self.maxHealth = maxHealth
        self.loot = loot

    #The fight function takes a random number from the characters power range and subtracts it from the other
    def fight(self, other):
        atk = random.randrange(0, self.power)
        other.health -= atk
        print(f"{self.name} attacks {other.name} for {atk} HP.")

    # Initialize player and monsters
player = GameCharacter("Adventurer", 20, 80, 80, 0)

monster1 = GameCharacter("Goblin", 10, 20, 20, 3)
monster2 = GameCharacter("Orc", 17, 30, 30, 5)
monster3 = GameCharacter("Giant Spider", 12, 25, 25, 4)
monster4 = GameCharacter("Slime", 5, 40, 40, 3)
monster5 = GameCharacter("Dragon", 20, 35, 35, 8)
monsterList = [monster1, monster2, monster3, monster4, monster5]

    #Player character progress saving. In the works pending research
"""
def save_health(self, filename):
    with open(filename, "wb") as hFile:
        p.dump(self.health, hFile)

def load_distance(self, filename):
    try:
        save_dir = os.path.join("Adventures_Rush", "Saved_Game")
        with open(os.path.join(save_dir, "distance.pk1"), "rb") as dFile:
            self.distance = p.load(dFile)
    except FileNotFoundError:
        print("No saved distance file found. Using default distance.")

def load_MonsterSlain(self, filename):
    try:
        save_dir = os.path.join("Adventures_Rush", "Saved_Game")
        with open(os.path.join(save_dir, "MonsterSlain.pk1"), "rb") as mFile:
            self.MonsterSlain = p.load(mFile)
    except FileNotFoundError:
        print("No saved monster slain file found. Using default monster slain.")

def load_inventory(self, filename):
    try:
        save_dir = os.path.join("Adventures_Rush", "Saved_Game")
        with open(os.path.join(save_dir, "inventory.pk1"), "rb") as iFile:
            self.inventory = p.load(iFile)
    except FileNotFoundError:
        print("No saved inventory file found. Using default inventory.")

def load_health(self, filename):
    try:
        save_dir = os.path.join("Adventures_Rush", "Saved_Game")
        with open(os.path.join(save_dir, "health.pk1"), "rb") as hFile:
            self.health = p.load(hFile)
    except FileNotFoundError:
        print("No saved health file found. Using default health.")
        """