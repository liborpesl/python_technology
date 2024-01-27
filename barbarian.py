class Barbarian:
    def __init__(self, strength, stamina, weapon):
        self.health = 100
        self.strength = strength
        self.stamina = stamina
        self.weapon = weapon
        self.weapon = weapon
        self.weapon = weapon

    # ctrl + D
    # alt + 1
    # alt +  tab nebo control + tab
    #

    def attack(self):
        damage = self.weapon.attack() + self.strength

        if damage > 15 and self.strength > 50 and self.stamina > 50:
            damage += 15
        elif self.stamina > 30:
            damage += 5

        return damage