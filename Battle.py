import re
import random
import Army
import Globals
class Battle:
        
        battlePhase = 0
        
        def run_round(self,army1,army2,roundCount):
                phase = 'Even'

                
                roundmessage = "##**Round {}** \n \n".format(roundCount)
                roll1 = army1.attack_roll()
                roll2 = army2.attack_roll()
                roundmessage += "**{}** Roll: {} ({}{:+})\n \n".format(army1.name,roll1,roll1-army1.bonus,army1.bonus)
                roundmessage += "**{}** Roll: {} ({}{:+})\n \n".format(army2.name,roll2,roll2-army2.bonus,army2.bonus)

                #fun bit of code to determine which phase it is. Logs it in battlePhase, attacker winning adds numbers, defender subtracts with 0 being even
                if(roll1 > roll2):
                        difference = roll1-roll2
                        if(difference >= 75):
                                self.battlePhase += 2
                                roundmessage += "The {} army pushes the {} army back, dealing a massive blow.\n \n".format(army1.name,army2.name)
                        elif(difference >= 25):
                                self.battlePhase += 1
                                roundmessage += "The {} army pushes the {} army back, dealing minor damage.\n \n".format(army1.name,army2.name)
                        else:
                                 roundmessage += "Both armies are equal. \n \n"
                        if(self.battlePhase >= 3):
                                 #Logs that the army cannot fight, bringing the battle to an end.
                                 army2.continueFighting = False
                                 roundmessage += "{} defeats {}, bringing an end to the battle.\n \n".format(army1.name,army2.name)
                                 roundmessage += "**Winner: {}**\n \n".format(army1.name)
                                 roundmessage += "Rounds taken: {} \n \n".format(roundCount)
                                 

                elif(roll2 > roll1):
                        difference = roll2-roll1
                        if(difference >= 75):
                                self.battlePhase -= 2
                                roundmessage += "The {} army pushes the {} army back, dealing a massive blow.\n \n".format(army2.name,army1.name)
                        elif(difference >= 25):
                                self.battlePhase -= 1
                                roundmessage += "The {} army pushes the {} army back, dealing minor damage.\n \n".format(army2.name,army1.name)
                        else:
                                 roundmessage += "Both armies are equal. \n \n"
                        if(self.battlePhase <= -3):
                                 army1.continueFighting = False
                                 roundmessage += "{} defeats {}, bringing an end to the battle.\n \n \n".format(army2.name,army1.name)
                                 roundmessage += "**Winner: {}**\n \n".format(army2.name)
                                 roundmessage += "Rounds taken: {} \n \n".format(roundCount)

                                 
            
                #Godamn python globals. Logs the phase to print out and calculate casualties. Each pass through will add casualties onto the previous, making the total.
                global attackcas
                global defendcas
                if(self.battlePhase >= 3):
                    phase = 'Defender Routing'
                    roundmessage += "##**Phase - Defender Routing** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 0
                    if(Globals.battleType == "Naval"):
                            defendcas += 8
                            print("Navy")
                    else:
                            defendcas += 25
                elif(self.battlePhase == 2):
                    phase = 'Defender Breaking'
                    roundmessage += "##**Phase - {}** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 0.25
                    defendcas += 4
                elif(self.battlePhase == 1):
                    phase = 'Defender Losing'
                    roundmessage += "##**Phase - {}** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 0.5
                    defendcas += 2
                elif(self.battlePhase == 0):
                    phase = 'Even'
                    roundmessage += "##**Phase - {}** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 1
                    defendcas += 1
                elif(self.battlePhase == -1):
                    phase = 'Attacker Losing'
                    roundmessage += "##**Phase - {}** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 2
                    defendcas += 0.5
                elif(self.battlePhase == -2):
                    phase = 'Attacker Breaking'
                    roundmessage += "##**Phase - {}** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    attackcas += 4
                    defendcas += 0.25
                elif(self.battlePhase <= -3):
                    phase = 'Attacker Routing'
                    roundmessage += "##**Phase - Attacker Routing** \n \n".format(phase)
                    roundmessage += "--- \n \n"
                    defendcas += 0
                    if(Globals.battleType == "Naval"):
                            attackcas += 8
                            print("Navy")
                    else:
                            attackcas += 25

                return roundmessage
        
            

        def run(self,battleInfo):
                roundCount = 1
                global attackcas
                global defendcas
                attackcas = 0
                defendcas = 0
                
                
                army1 = Army.Army(battleInfo.group(1),int(battleInfo.group(2)),int (battleInfo.group(3)))
                army2 = Army.Army(battleInfo.group(4),int(battleInfo.group(5)),int (battleInfo.group(6)))

                if(Globals.battleType == "Naval"):
                        battlemessage = "#Naval Battle Between {} and {} \n \n".format(army1.name,army2.name)
                else:
                        battlemessage = "#Land Battle Between {} and {} \n \n".format(army1.name,army2.name)
                battlemessage += "*I am a bot by dinoking. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                battlemessage += "--- \n \n"
                
                battlemessage += self.run_round(army1,army2,roundCount)

                while(army1.continueFighting and army2.continueFighting):
                        roundCount += 1
                        battlemessage += self.run_round(army1,army2,roundCount)
                        
                battlemessage += "#**Casualties** \n \n".format(army1.name,army2.name)
                battlemessage += "{} Casualties = {}% \n \n{} Casualties = {}%\n \n".format(army1.name,attackcas,army2.name,defendcas)
                battlemessage += "(Note this doesn't include commander bonuses, so please take that percentage away from the total)\n \n"
                battlemessage += "--- \n \n"         

                return battlemessage
                print ("Finished battle")
                self.reset_battle_phase()
                
        def reset_battle_phase(self):
                self.battlePhase = 0
