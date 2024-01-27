# mockovani
# mock
import random


class Weapon:
    def __init__(self, strength, endurance, health, width, height):
        self.strength = strength
        self.endurance = endurance
        self.health = health
        self.width = width
        self.height = height

    def attack(self):
        if self.health < 10:
            raise Exception("Mas to rozbite!")

        value = random.randint(0, self.endurance)

        # print(value, (self.endurance // 2))

        if value < (self.endurance // 2):  # 8
            self.health += 1

        bonus_damage = random.randint(0, 20)  # 2

        return self.strength + bonus_damage