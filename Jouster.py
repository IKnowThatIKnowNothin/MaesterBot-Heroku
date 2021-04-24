import re
import random
class Jouster:
        name = ""
        bonus = 0
        injuryRoll = 0
        continueFighting = True
        ableToFight = True
        brokenLances = 0
        minorInjuries = 0
        moderateInjuries = 0
        majorInjuries = 0
        permanentInjuries = "None"
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
                if(injuryRoll >= 16):
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                elif(injuryRoll >= 10):
                        self.minorInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                elif(injuryRoll >= 6):
                        self.moderateInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                else:
                        self.majorInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
        def death_roll(self):
                injuryRoll = random.randint(1,20)
                if(injuryRoll >= 16):
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                elif(injuryRoll >= 10):
                        self.minorInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                elif(injuryRoll >= 6):
                        self.moderateInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                elif(injuryRoll >=3):
                        self.majorInjuries += 1
                        self.continueFighting = False
                        self.ableToFight = False
                        return 0
                else:
                        self.continueFighting = False
                        self.ableToFight = False
                        permanentRoll = random.randint(1,100)
                        if (permanentRoll <= 25):
                                self.alive = False
                        elif (permanentRoll <= 40):
                                self.permanentInjuries = "Hand"
                        elif (permanentRoll <= 55):
                                self.permanentInjuries = "Foot"
                        elif (permanentRoll <= 65):
                                self.permanentInjuries = "Blinded"
                        elif (permanentRoll <= 75):
                                self.permanentInjuries = "Defeaned"
                        elif (permanentRoll <= 40):
                                self.permanentInjuries = "Internal"
                        elif (permanentRoll <= 40):
                                self.permanentInjuries = "Scar"
                        else:
                                self.permanentInjuries = "Genital"
                        print(permanentRoll)
                        print(self.permanentInjuries)
                        return 0
