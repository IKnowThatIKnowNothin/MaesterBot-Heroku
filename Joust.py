import re
import random
import Jouster
import Globals
class Joust:
        
        joustPhase = 0
        phaseDifference = 0
        Globals.message = 1
        
        
        def run_round(self,jouster1,jouster2,roundCount):
                
                roundmessage = "##**Tilt {}** \n \n".format(roundCount+1)
                roll1 = jouster1.attack_roll()
                roll2 = jouster2.attack_roll()
                unmodded1 = roll1-jouster1.bonus
                unmodded2 = roll2-jouster2.bonus
                roundmessage += "**{}** Roll: {} ({}{:+})\n \n".format(jouster1.name,roll1,unmodded1,jouster1.bonus)
                roundmessage += "**{}** Roll: {} ({}{:+})\n \n".format(jouster2.name,roll2,unmodded2,jouster2.bonus)

                if(roll1 > roll2):
                        difference = roll1-roll2
                        unmoddedDiff = unmodded1-unmodded2

                        if(unmoddedDiff >= 95):
                                jouster2.death_roll()
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, injuring them and bringing an end to the joust.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, injuring them and bringing an end to the joust.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing {}.\n \n".format(jouster1.name,jouster2.name)

                        elif(difference >= 90):
                                jouster2.injury_roll()
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, injuring them and bringing an end to the joust.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, injuring them and bringing an end to the joust.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing {}.\n \n".format(jouster1.name,jouster2.name)

                        elif(difference >= 75):
                                jouster2.continueFighting = False
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, bringing an end to the joust.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, bringing an end to the joust.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, unhorsing their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, unhorsing {}.\n \n".format(jouster1.name,jouster2.name)

                        elif(difference >= 55):
                                jouster1.brokenLances += 1
                                jouster1.bonus += 9
                                if (jouster1.brokenLances >= 3):
                                        jouster2.continueFighting = False
                                        roundmessage += "{} breaks their final lance against {}, bringing an end to the joust.\n\n".format(jouster1.name,jouster2.name)
                                elif(jouster1.brokenLances >= 2):
                                        roundmessage += "{} breaks their second lance against {}, bringing them one step closer to victory.\n\n".format(jouster1.name,jouster2.name)
                                else:
                                        roundmessage += "{} breaks their first lance against {}, bringing them one step closer to victory.\n\n".format(jouster1.name,jouster2.name)

                        elif(difference >= 35):
                                jouster1.bonus += 5
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} lands a strong hit on their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} lands a strong hit against {}.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to land a strong hit against their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} manages to land a strong hit against {}.\n \n".format(jouster1.name,jouster2.name)
                     
                        elif(difference >= 15):
                                jouster1.bonus += 2
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} lands a hit on their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} lands a hit against {}.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to land a hit against their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} manages to land a hit against {}.\n \n".format(jouster1.name,jouster2.name)
                                
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} aims wide and misses their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} aims wide and misses {}.\n \n".format(jouster1.name,jouster2.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} only manages a glancing blow against their opponent.\n \n".format(jouster1.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} only manages a glancing blow against {}.\n \n".format(jouster1.name,jouster2.name)
                                 

                else:
                        difference = roll2-roll1
                        unmoddedDiff = unmodded2-unmodded1
                        
                        if(unmoddedDiff >= 95):
                                jouster1.death_roll()
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, injuring them and bringing an end to the joust.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, injuring them and bringing an end to the joust.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing {}.\n \n".format(jouster2.name,jouster1.name)

                        elif(difference >= 90):
                                jouster1.injury_roll()
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, injuring them and bringing an end to the joust.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, injuring them and bringing an end to the joust.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, injuring and unhorsing {}.\n \n".format(jouster2.name,jouster1.name)

                        elif(difference >= 75):
                                jouster1.continueFighting = False
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} manages to unhorse their opponent, bringing an end to the joust.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} manages to unhorse {}, bringing an end to the joust.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} aims their lance just right, unhorsing their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} aims their lance just right, unhorsing {}.\n \n".format(jouster2.name,jouster1.name)

                        elif(difference >= 55):
                                jouster2.brokenLances += 1
                                jouster2.bonus += 9
                                if (jouster2.brokenLances >= 3):
                                        roundmessage += "{} breaks their final lance against {}, bringing an end to the joust.\n\n".format(jouster2.name,jouster1.name)
                                        jouster1.continueFighting = False
                                elif(jouster2.brokenLances >= 2):
                                        roundmessage += "{} breaks their second lance against {}, bringing them one step closer to victory.\n\n".format(jouster2.name,jouster1.name)
                                else:
                                        roundmessage += "{} breaks their first lance against {}, bringing them one step closer to victory.\n\n".format(jouster2.name,jouster1.name)

                        elif(difference >= 35):
                                jouster2.bonus += 5
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} lands a strong hit on their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} lands a strong hit against {}.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to land a strong hit against their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} manages to land a strong hit against {}.\n \n".format(jouster2.name,jouster1.name)
                     
                        elif(difference >= 15):
                                jouster2.bonus += 2
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} lands a hit on their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} lands a hit against {}.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} manages to land a hit against their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} manages to land a hit against {}.\n \n".format(jouster2.name,jouster1.name)
                                
                        else:
                                Globals.message = self.numberGen(4)
                                if(Globals.message == 1):
                                        roundmessage += "{} aims wide and misses their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 2):
                                        roundmessage += "{} aims wide and misses {}.\n \n".format(jouster2.name,jouster1.name)
                                elif(Globals.message == 3):
                                        roundmessage += "{} only manages a glancing blow against their opponent.\n \n".format(jouster2.name)
                                elif(Globals.message == 4):
                                        roundmessage += "{} only manages a glancing blow against {}.\n \n".format(jouster2.name,jouster1.name)
                                
                                
                roundmessage += "--- \n \n"
                return roundmessage


        def numberGen(self,maxCount):
                newMessage = random.randint(1,maxCount)
                message2 = Globals.message
                while (newMessage == message2):
                        newMessage = random.randint(1,maxCount)
                return newMessage
                        
        
        def run(self,joustInfo):
                roundCount = 0
                
                if(joustInfo.group(2)):
                        group2 = joustInfo.group(2)
                else:
                        group2 = 0
                if(joustInfo.group(4)):
                        group4 = joustInfo.group(4)
                else:
                        group4 = 0
                
                jouster1 = Jouster.Jouster(joustInfo.group(1), int(group2))
                jouster2 = Jouster.Jouster(joustInfo.group(3), int(group4))
                battlemessage = "#Joust Between {} and {} \n \n".format(jouster1.name,jouster2.name)
                battlemessage += "*I am a bot managed and run by the r/CenturyOfBlood modteam. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                battlemessage += "--- \n \n"
                notbattlemessage = ""
                roundOver = True
                while(jouster1.continueFighting and jouster2.continueFighting and roundOver):
                        if(Globals.resultsMode):
                                notbattlemessage += self.run_round(jouster1,jouster2,roundCount)
                                roundCount += 1
                                if(roundCount == 7):
                                        if(Globals.battleType != "Continued"):
                                                if(jouster1.continueFighting and jouster2.continueFighting):
                                                        roundOver = False
                        else:
                                battlemessage += self.run_round(jouster1,jouster2,roundCount)
                                roundCount += 1
                                if(roundCount == 7):
                                        if(Globals.battleType != "Continued"):
                                                if(jouster1.continueFighting and jouster2.continueFighting):
                                                        roundOver = False
                        
                if(not roundOver):
                        battlemessage += "**After seven tilts, the Joust ends in a draw.**\n \n"
                elif(jouster1.continueFighting):
                        battlemessage += "**Winner: {}**\n \n".format(jouster1.name)
                else:
                        battlemessage += "**Winner: {}**\n \n".format(jouster2.name)
                battlemessage += "Tilts taken: {} \n \n".format(roundCount)

                if(jouster1.alive == False):
                        battlemessage += "{} is killed in the joust.\n\n".format(jouster1.name)
                elif(jouster2.alive == False):
                        battlemessage += "{} is killed in the joust.\n\n".format(jouster2.name)
                else:
                        
                        if(jouster1.injuryRoll != 0):
                                if(jouster1.permanentInjuries != "None"):
                                        if(jouster1.permanentInjuries == "Hand"):
                                                battlemessage += "{} suffers a permanent injury and loses a hand/arm in the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Foot"):
                                                battlemessage += "{} suffers a permanent injury and loses a leg/foot in the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Blinded"):
                                                battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Deafened"):
                                                battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Internal"):
                                                battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Scar"):
                                                battlemessage += "{} suffers a permanent injury and gets intensely scarred from the joust.\n\n".format(jouster1.name)
                                        elif(jouster1.permanentInjuries == "Genital"):
                                                battlemessage += "{} suffers a permanent injury and suffers a genital wound from the joust.\n\n".format(jouster1.name)
                                else:
                                        battlemessage += "{} emerges from the joust with {} major, {} moderate and {} minor injuries.\n\n".format(jouster1.name,jouster1.majorInjuries,jouster1.moderateInjuries,jouster1.minorInjuries)

                        elif(jouster2.injuryRoll != 0):
                                if(jouster2.permanentInjuries != "None"):
                                        if(jouster2.permanentInjuries == "Hand"):
                                                battlemessage += "{} suffers a permanent injury and loses a hand/arm in the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Foot"):
                                                battlemessage += "{} suffers a permanent injury and loses a leg/foot in the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Blinded"):
                                                battlemessage += "{} suffers a permanent injury and is permanently blinded in one eye from the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Deafened"):
                                                battlemessage += "{} suffers a permanent injury and is partially/fully loses their hearing from the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Internal"):
                                                battlemessage += "{} suffers a permanent injury and suffers internal organ damage from the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Scar"):
                                                battlemessage += "{} suffers a permanent injury and gets intensely scarred from the joust.\n\n".format(jouster2.name)
                                        elif(jouster2.permanentInjuries == "Genital"):
                                                battlemessage += "{} suffers a permanent injury and suffers a genital wound from the joust.\n\n".format(jouster2.name)
                                else:
                                        battlemessage += "{} emerges from the joust with {} major, {} moderate and {} minor injuries.\n\n".format(jouster2.name,jouster2.majorInjuries,jouster2.moderateInjuries,jouster2.minorInjuries)
                        


                        
                ##reset_duel_phase()
                self.joustPhase = 0
                return battlemessage
        
        def reset_joust_phase(self):
                self.joustPhase = 0
