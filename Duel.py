import re
import random
import Dueler
import Globals
class Duel:
        
        duelPhase = 0
        phaseDifference = 0
        Globals.message = 1
        
        
        def run_round(self,dueler1,dueler2,roundCount):
                
                roundmessage = "##**Round {}** \n \n".format(roundCount+1)
                roll1 = dueler1.attack_roll()
                roll2 = dueler2.attack_roll()
                roundmessage += "**{}** Roll: {} ({:+})\n \n".format(dueler1.name,roll1-dueler1.bonus,dueler1.bonus)
                roundmessage += "**{}** Roll: {} ({:+})\n \n".format(dueler2.name,roll2-dueler2.bonus,dueler2.bonus)

                if(roll1 > roll2):
                        difference = roll1-roll2

                        self.phaseDifference = 0
                        if(difference > 44):
                                self.duelPhase += 1
                                self.phaseDifference = 1

                        if(difference > 89):
                                self.duelPhase += 10
                                if(Globals.battleType == "Live"):
                                        dueler1.bonus += dueler2.death_roll()
                                else:
                                        dueler1.bonus += dueler2.blunted_roll()
                                roundmessage += "{} breaks {}, bringing an end to the duel.\n \n".format(dueler1.name,dueler2.name)
                                roundmessage += "##**Phase - {} Broken** \n \n".format(dueler2.name)


                        elif(self.duelPhase >= 3):
                                 if (Globals.battleType == "Live Duel"):
                                         dueler1.bonus += dueler2.broken_roll()
                                 else:
                                         dueler1.bonus += dueler2.blunted_roll()
                                 roundmessage += "{} defeats {}, bringing an end to the duel.\n \n".format(dueler1.name,dueler2.name)
                                 roundmessage += "##**Phase - {} Broken** \n \n".format(dueler2.name)
                                 

                else:
                        difference = roll2-roll1
                        
                        self.phaseDifference = 0
                        if(difference > 44):
                                self.duelPhase -= 1
                                self.phaseDifference = -1

                        if(difference > 89):
                                self.duelPhase -= 10
                                if(Globals.battleType == "Live"):
                                        dueler2.bonus += dueler1.death_roll()
                                else:
                                        dueler2.bonus += dueler1.blunted_roll()
                                roundmessage += "{} breaks {}, bringing an end to the duel.\n \n".format(dueler2.name,dueler1.name)
                                roundmessage += "##**Phase - {} Broken** \n \n".format(dueler1.name)


                        elif(self.duelPhase <= -3):
                                if (Globals.battleType == "Live Duel"):
                                        dueler2.bonus += dueler1.broken_roll()
                                else:
                                        dueler2.bonus += dueler1.blunted_roll()
                                roundmessage += "{} defeats {}, bringing an end to the duel.\n \n".format(dueler2.name,dueler1.name)
                                roundmessage += "##**Phase - {} Broken** \n \n".format(dueler1.name)




                if(self.duelPhase == 2):
                        roll = dueler2.injury_roll()
                        dueler2.bonus -= roll
                        if (roll == 10):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} deflects a blow aimed at their head, and makes a quick thrust giving their opponent a moderate injury.\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} tries to lunge for their opponent, and recieves a moderate injury for their effort.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} overpowers their opponent and manages to give them a moderate injury.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} leaves themselves open, gaining a moderate injury.\n \n".format(dueler2.name)
                        elif (roll == 5):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} makes a quick attack, leaving their opponent with a minor injury.\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} parries a blow and gives their opponent a minor injury.\n \n".format(dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} quickly lunges, managing to give their opponent a minor injury.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} is a fraction too slow to avoid their opponents blow, getting a minor injury.\n \n".format(dueler2.name)
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} narrowly dodges their opponent's blow.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} parries a blow aimed at their head.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to turn aside a blow meant for their arm.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their blow a bit too high, missing {}.\n \n".format(dueler1.name,dueler2.name)
                                        
                        roundmessage += "##**Phase - {} Injured** \n \n".format(dueler2.name)


                        
                elif(self.duelPhase == -2):
                        roll = dueler1.injury_roll()
                        dueler1.bonus -= roll
                        if (roll == 10):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} deflects a blow aimed at their head, and makes a quick thrust giving their opponent a moderate injury.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} tries to lunge for their opponent, and recieves a moderate injury for their effort.\n \n".format(dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} overpowers their opponent and manages to give them a moderate injury.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} leaves themselves open, gaining a moderate injury.\n \n".format(dueler1.name)
                        elif (roll == 5):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} makes a quick attack, leaving their opponent with a minor injury.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} parries a blow and gives their opponent a minor injury.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} quickly lunges, managing to give their opponent a minor injury.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} is a fraction too slow to avoid their opponents blow, getting a minor injury.\n \n".format(dueler1.name)
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} narrowly dodges their opponent's blow.\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} parries a blow aimed at their head.\n \n".format(dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to turn aside a blow meant for their arm.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their blow a bit too high, missing {}.\n \n".format(dueler2.name,dueler1.name)
                                        

                        roundmessage += "##**Phase - {} Injured** \n \n".format(dueler1.name)

              
                                        
                elif(self.duelPhase == 1):
                        if(self.phaseDifference == 1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler2.name,dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler1.name,dueler2.name)
                        elif(self.phaseDifference == -1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler1.name,dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler2.name,dueler1.name)
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler1.name)        

                        roundmessage += "##**Phase - {} Losing** \n \n".format(dueler2.name)

        
                        
                elif(self.duelPhase == -1):
                        if(self.phaseDifference == 1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler2.name,dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler1.name,dueler2.name)
                        elif(self.phaseDifference == -1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler1.name,dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler2.name,dueler1.name)
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler1.name)        

                        roundmessage += "##**Phase - {} Losing** \n \n".format(dueler1.name)

                        

                elif(self.duelPhase == 0):
                        if(self.phaseDifference == 1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler2.name,dueler1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler1.name,dueler2.name)
                        elif(self.phaseDifference == -1):
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} pushes their opponent back\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} leaps backwards to avoid {}'s oncoming blows.\n \n".format(dueler1.name,dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sweeps under their opponent's guard, pushing them backwards.\n \n".format(dueler2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} sidesteps {}, forcing them to readjust their guard.\n \n".format(dueler2.name,dueler1.name)
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} sidesteps an oncoming blow and delivers one back in return.\n \n".format(dueler1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} exchanges blows with their opponent, neither side letting up.\n \n".format(dueler1.name)        

                        roundmessage += "##**Phase - Even** \n \n"



                                
                roundmessage += "--- \n \n"
                return roundmessage


        def numberGen(self,maxCount):
                newMessage = random.randint(1,maxCount)
                message2 = Globals.message
                while (newMessage == message2):
                        newMessage = random.randint(1,maxCount)
                return newMessage
                        
        
        def run(self,duelInfo):
                roundCount = 0

                                
                if(duelInfo.group(2)):
                        group2 = duelInfo.group(2)
                else:
                        group2 = 0
                if(duelInfo.group(4)):
                        group4 = duelInfo.group(4)
                else:
                        group4 = 0
                
                dueler1 = Dueler.Dueler(duelInfo.group(1), int(group2))
                dueler2 = Dueler.Dueler(duelInfo.group(3), int(group4))
                battlemessage = "#Duel Between {} and {} \n \n".format(dueler1.name,dueler2.name)
                battlemessage += "*I am a bot by Skuldakn. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                battlemessage += "--- \n \n"
                notbattlemessage = ""
                while(dueler1.continueFighting and dueler2.continueFighting):
                        if(Globals.resultsMode):
                                notbattlemessage += self.run_round(dueler1,dueler2,roundCount)
                                roundCount += 1
                        else:
                                battlemessage += self.run_round(dueler1,dueler2,roundCount)
                                roundCount += 1
                        
                if(dueler1.continueFighting):
                        battlemessage += "**Winner: {}**\n \n".format(dueler1.name)
                else:
                        battlemessage += "**Winner: {}**\n \n".format(dueler2.name)
                battlemessage += "Rounds taken: {} \n \n".format(roundCount)
                
                if(dueler1.alive == False and dueler2.alive == False):
                        battlemessage += "Both combatants are killed in the duel.\n\n"
                if(dueler1.alive == False):
                        battlemessage += "{} is killed in the duel. Their opponent emerges with {} major, {} moderate and {} minor injuries.\n\n".format(dueler1.name,dueler2.majorInjuries,dueler2.moderateInjuries,dueler2.minorInjuries)
                        if(dueler2.permanentInjuries != "None"):
                                if(dueler2.permanentInjuries == "Hand"):
                                        battlemessage += "{} suffers a permanent injury and loses a hand/arm in the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Foot"):
                                        battlemessage += "{} suffers a permanent injury and loses a leg/foot in the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Blinded"):
                                        battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Deafened"):
                                        battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Internal"):
                                        battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Scar"):
                                        battlemessage += "{} suffers a permanent injury and gets intensely scarred from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Genital"):
                                        battlemessage += "{} suffers a permanent injury and suffers a genital wound from the duel.\n\n".format(dueler2.name)
                elif(dueler2.alive == False):
                        battlemessage += "{} is killed in the duel. Their opponent emerges with {} major, {} moderate and {} minor injuries.\n\n".format(dueler2.name,dueler1.majorInjuries,dueler1.moderateInjuries,dueler1.minorInjuries)
                        if(dueler1.permanentInjuries != "None"):
                                if(dueler1.permanentInjuries == "Hand"):
                                        battlemessage += "{} suffers a permanent injury and loses a hand/arm in the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Foot"):
                                        battlemessage += "{} suffers a permanent injury and loses a leg/foot in the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Blinded"):
                                        battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Deafened"):
                                        battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Internal"):
                                        battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Scar"):
                                        battlemessage += "{} suffers a permanent injury and gets intensely scarred from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Genital"):
                                        battlemessage += "{} suffers a permanent injury and suffers a genital wound from the duel.\n\n".format(dueler1.name)
                else:
                        battlemessage += "{} emerges from the duel with {} major, {} moderate and {} minor injuries.\n\n".format(dueler1.name,dueler1.majorInjuries,dueler1.moderateInjuries,dueler1.minorInjuries)
                        if(dueler1.permanentInjuries != "None"):
                                if(dueler1.permanentInjuries == "Hand"):
                                        battlemessage += "{} suffers a permanent injury and loses a hand/arm in the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Foot"):
                                        battlemessage += "{} suffers a permanent injury and loses a leg/foot in the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Blinded"):
                                        battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Deafened"):
                                        battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Internal"):
                                        battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Scar"):
                                        battlemessage += "{} suffers a permanent injury and gets intensely scarred from the duel.\n\n".format(dueler1.name)
                                elif(dueler1.permanentInjuries == "Genital"):
                                        battlemessage += "{} suffers a permanent injury and suffers a genital wound from the duel.\n\n".format(dueler1.name)
                        battlemessage += "{} emerges from the duel with {} major, {} moderate and {} minor injuries.\n\n".format(dueler2.name,dueler2.majorInjuries,dueler2.moderateInjuries,dueler2.minorInjuries)
                        if(dueler2.permanentInjuries != "None"):
                                if(dueler2.permanentInjuries == "Hand"):
                                        battlemessage += "{} suffers a permanent injury and loses a hand/arm in the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Foot"):
                                        battlemessage += "{} suffers a permanent injury and loses a leg/foot in the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Blinded"):
                                        battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Deafened"):
                                        battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Internal"):
                                        battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Scar"):
                                        battlemessage += "{} suffers a permanent injury and gets intensely scarred from the duel.\n\n".format(dueler2.name)
                                elif(dueler2.permanentInjuries == "Genital"):
                                        battlemessage += "{} suffers a permanent injury and suffers a genital wound from the duel.\n\n".format(dueler2.name)
  


                        
                ##reset_duel_phase()
                self.duelPhase = 0
                return battlemessage
        
        def reset_duel_phase(self):
                self.duelPhase = 0
