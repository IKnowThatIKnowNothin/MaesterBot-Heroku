import re
import random
class Dueler:
	name = ""
	bonus = 0
	continueFighting = True
	ableToFight = True
	minorInjuries = 0
	moderateInjuries = 0
	majorInjuries = 0
	alive = True
	def __init__(self,name,bonus):
		self.name = name
		self.bonus = bonus
	def attack_roll(self):
		return random.randint(1,100) + self.bonus
	def modify_bonus(self,mod):
		self.bonus += mod
	def injury_roll(self):
		injuryRoll = random.randint(1,20)
		if(injuryRoll > 15):
			self.moderateInjuries += 1
			return 10
		elif(injuryRoll > 5):
			self.minorInjuries += 1
			return 5
		else:
			return 0
	def death_roll(self):
		deathRoll = random.randint(1,20)
		if(deathRoll > 15):
			self.majorInjuries += 1
			self.continueFighting = False
			return 20
		elif(deathRoll > 1):
			self.continueFighting = False
			self.ableToFight = False
			return 0
		else:
			self.continueFighting = False
			self.ableToFight = False
			self.alive = False
			return 0
	def broken_roll(self):
		brokenRoll = random.randint(1,20)
		if(brokenRoll > 18):
			self.majorInjuries += 1
			self.continueFighting = False
			return 20
		else:
			self.continueFighting = False
			self.ableToFight = False
			return 0
