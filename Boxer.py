import re
import random
class Boxer:
        name = ""
        bonus = 0
        malus = 0
        ableToFight = True

        def __init__(self,name,bonus):
                self.name = name
                self.health = bonus
        def attack_roll(self):
                return random.randint(1,10) - self.malus
