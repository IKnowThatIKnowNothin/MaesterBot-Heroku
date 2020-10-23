import re
import random
import Boxer
import Globals
class Boxing:
        
        duelPhase = 0
        Globals.message = 1
        
        
        def run_round(self,boxer1,boxer2,roundCount):
                
                roundmessage = "##**Round {}** \n \n".format(roundCount+1)
                roll1 = boxer1.attack_roll()
                roll2 = boxer2.attack_roll()

                if(roll1 < 1):
                        roll1 = 1
                if(roll2 < 1):
                        roll2 = 1

                boxer1.health -= roll2
                boxer2.health -= roll1
                
                roundmessage += "**{}** Health: {} Roll: {} (-{})\n \n".format(boxer1.name,boxer1.health,roll1,boxer1.malus)
                roundmessage += "**{}** Health: {} Roll: {} (-{})\n \n".format(boxer2.name,boxer2.health,roll2,boxer2.malus)

                if(roll1 > roll2):
                        difference = roll1-roll2

                        if(difference > 8):
                                boxer2.ableToFight = False
                                if(boxer1.health <= 0):
                                        boxer1.ableToFight = False
                                        roundmessage += "{} knocks out {}, but the effort overwhelms them and they fall unconcious.\n \n".format(boxer1.name,boxer2.name)
                                else:
                                        roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer1.name,boxer2.name)

                                        

                        elif(boxer1.health <= 0):
                                boxer1.ableToFight = False
                                if(boxer2.health <= 0):
                                        boxer2.ableToFight = False
                                        roundmessage += "Both contestants fall from exhaustion.\n \n".format(boxer1.name,boxer2.name)
                                else:
                                        roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer2.name,boxer1.name)
                                
                        elif(boxer2.health <= 0):
                                boxer2.ableToFight = False
                                roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer1.name,boxer2.name)

                        elif(difference > 7):
                                boxer2.malus += 2
                                roundmessage += "{} knocks down {}, who struggles to regain their footing.\n \n".format(boxer1.name,boxer2.name)

                        elif(difference > 6):
                                boxer2.malus += 1
                                roundmessage += "{} knocks down {}, who regains their footing immediately.\n \n".format(boxer1.name,boxer2.name)

                        else:
                                roundmessage += "Both fighters circle each other, looking for an opening\n \n"
                                 

                else:
                        difference = roll2-roll1

                        if(difference > 8):
                                boxer1.ableToFight = False
                                if(boxer2.health <= 0):
                                        boxer2.ableToFight = False
                                        roundmessage += "{} knocks out {}, but the effort overwhelms them and they fall unconcious.\n \n".format(boxer2.name,boxer1.name)
                                else:
                                        roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer2.name,boxer1.name)

                                        

                        elif(boxer1.health <= 0):
                                boxer1.ableToFight = False
                                if(boxer2.health <= 0):
                                        boxer2.ableToFight = False
                                        roundmessage += "Both contestants fall from exhaustion.\n \n".format(boxer1.name,boxer2.name)
                                else:
                                        roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer2.name,boxer1.name)
                                
                        elif(boxer2.health <= 0):
                                boxer2.ableToFight = False
                                roundmessage += "{} knocks out {}, bringing and end to the match\n \n".format(boxer1.name,boxer2.name)

                        elif(difference > 7):
                                boxer1.malus += 2
                                roundmessage += "{} knocks down {}, who struggles to regain their footing.\n \n".format(boxer2.name,boxer1.name)

                        elif(difference > 6):
                                boxer1.malus += 1
                                roundmessage += "{} knocks down {}, who regains their footing immediately.\n \n".format(boxer2.name,boxer1.name)

                        else:
                                roundmessage += "Both fighters circle each other, looking for an opening\n \n"

                if(boxer1.malus >= 5):
                        boxer1.ableToFight = False
                if(boxer2.malus >= 5):
                        boxer2.ableToFight = False
                        
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
                
                boxer1 = Boxer.Boxer(duelInfo.group(1), int(group2))
                boxer2 = Boxer.Boxer(duelInfo.group(3), int(group4))
                battlemessage = "#Boxing Match Between {} and {} \n \n".format(boxer1.name,boxer2.name)
                battlemessage += "*I am a bot by dino. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                battlemessage += "--- \n \n"
                while(boxer1.ableToFight and boxer2.ableToFight):
                        battlemessage += self.run_round(boxer1,boxer2,roundCount)
                        roundCount += 1
                        
                if(boxer1.ableToFight):
                        battlemessage += "**Winner: {}**\n \n".format(boxer1.name)
                elif(boxer2.ableToFight):
                        battlemessage += "**Winner: {}**\n \n".format(boxer2.name)
                else:
                        battlemessage += "**Draw!**\n\n"
                battlemessage += "Rounds taken: {} \n \n".format(roundCount)
                
                              ##reset_duel_phase()
                self.duelPhase = 0
                return battlemessage
        
        def reset_duel_phase(self):
                self.duelPhase = 0
