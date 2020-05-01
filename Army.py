import re
import random
class Army:
	name = ""
	power = 0
	bonus = 0
	continueFighting = True
	def __init__(self,name,power,bonus):
		self.name = name
		self.power = power
		self.bonus = bonus
	def attack_roll(self):
		return random.randint(1,100) +self.bonus
