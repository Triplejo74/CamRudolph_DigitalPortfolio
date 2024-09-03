# Characters.py
import random
import pickle as p

class GameCharacter:
    def __init__(self, name, power, health, loot):
        self.name = name
        self.power = power
        self.health = health
        self.loot = loot

    def fight(self, other):
        atk = random.randrange(0, self.power)
        other.health -= atk
        print(f"{self.name} attacks {other.name} for {atk} HP.")

    def save_health(self, filename):
        with open(filename, "wb") as hFile:
            p.dump(self.health, hFile)

    def load_health(self, filename):
        try:
            with open(filename, "rb") as hFile:
                self.health = p.load(hFile)
        except FileNotFoundError:
            print("No saved health file found. Using default health.")

# Initialize player and monsters
player = GameCharacter("Adventurer", 20, 80, 0)
player.load_health("health.pk1")

monster1 = GameCharacter("Goblin", 10, 20, 3)
monster2 = GameCharacter("Orc", 17, 30, 5)
monster3 = GameCharacter("Giant Spider", 12, 25, 4)
monster4 = GameCharacter("Slime", 5, 40, 3)
monster5 = GameCharacter("Dragon", 20, 35, 8)
monsterList = [monster1, monster2, monster3, monster4, monster5]
