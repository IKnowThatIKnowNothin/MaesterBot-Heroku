import re
import random
import Dueler
class Duel:
        duelPhase = 0
        def run_round(self,dueler1,dueler2,roundCount):
                roundmessage = "##**Round {}** \n \n".format(roundCount+1)
                roll1 = dueler1.attack_roll()
                roll2 = dueler2.attack_roll()
                roundmessage += "**{}** Roll: {} ({:+})\n \n".format(dueler1.name,roll1-dueler1.bonus,dueler1.bonus)
                roundmessage += "**{}** Roll: {} ({:+})\n \n".format(dueler2.name,roll2-dueler2.bonus,dueler2.bonus)
                if(roll1 > roll2):
                        difference = roll1-roll2
                        if(difference > 89):
                                dueler1.bonus += dueler2.death_roll()
                                roundmessage += "{} strikes hard, crushing {} and dealing a deathroll.\n \n".format(dueler1.name,dueler2.name)
                        elif(difference > 44):
                                self.duelPhase += 1
                                roundmessage += "{} pushes {} back.\n \n".format(dueler1.name,dueler2.name)
                        if(self.duelPhase == 2):
                                dueler1.bonus += dueler2.injury_roll()
                                roundmessage += "{} is vulnerable, leaving them open to injury.\n \n".format(dueler2.name)
                        elif(self.duelPhase == 3):
                                 dueler1.bonus += dueler2.broken_roll()
                                 roundmessage += "{} breaks {}, bringing an end to the duel.\n \n".format(dueler1.name,dueler2.name)
                if(roll2 > roll1):
                        difference = roll2-roll1
                        if(difference > 89):
                                dueler2.bonus += dueler1.death_roll()
                                roundmessage += "{} strikes hard, crushing {} and dealing a deathroll.\n \n".format(dueler2.name,dueler1.name)
                        elif(difference > 44):
                                self.duelPhase -= 1
                                roundmessage += "{} pushes {} back.\n \n".format(dueler2.name,dueler1.name)
                        if(self.duelPhase == -2):
                                dueler2.bonus += dueler1.injury_roll()
                                roundmessage += "{} is vulnerable, leaving them open to injury.\n \n".format(dueler1.name)
                        elif(self.duelPhase == -3):
                                dueler2.bonus += dueler1.broken_roll()
                                roundmessage += "{} breaks {}, bringing an end to the duel.\n \n".format(dueler2.name,dueler1.name)
                roundmessage += "--- \n \n"
                return roundmessage
        def run(self,duelInfo):
                roundCount = 0
                dueler1 = Dueler.Dueler(duelInfo.group(1),int(duelInfo.group(2)))
                dueler2 = Dueler.Dueler(duelInfo.group(3),int(duelInfo.group(4)))
                battlemessage = "#Duel Between {} and {} \n \n".format(dueler1.name,dueler2.name)
                battlemessage += "*I am a bot by Skuldakn. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                battlemessage += "--- \n \n"
                while(dueler1.continueFighting and dueler2.continueFighting):
                        battlemessage += self.run_round(dueler1,dueler2,roundCount)
                        roundCount += 1
                if(dueler1.continueFighting):
                        battlemessage += "**Winner: {}**\n \n".format(dueler1.name)
                else:
                        battlemessage += "**Winner: {}**\n \n".format(dueler2.name)
                battlemessage += "Rounds taken: {} \n \n".format(roundCount)
                battlemessage += "**{}:** Bonus: {} - Alive: {} - Can Continue Fighting: {} - Minor Injuries: {} - Moderate Injuries: {} - Major Injuries: {}\n \n".format(dueler1.name,dueler1.bonus,dueler1.alive,dueler1.ableToFight,dueler1.minorInjuries,dueler1.moderateInjuries,dueler1.majorInjuries)
                battlemessage += "**{}:** Bonus: {} - Alive: {} - Can Continue Fighting: {} - Minor Injuries: {} - Moderate Injuries: {} - Major Injuries: {}\n \n".format(dueler2.name,dueler2.bonus,dueler2.alive,dueler2.ableToFight,dueler2.minorInjuries,dueler2.moderateInjuries,dueler2.majorInjuries)
                self.reset_duel_phase()
                return battlemessage
        def reset_duel_phase(self):
                self.duelPhase = 0
