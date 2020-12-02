import praw
import re
import Battle
import Duel
import Boxing
import time
import Army
import random
import Globals



intro = random.randint(1,4)
if (intro == 1):
    print ("I'm afraid I can't do that Dave.")
    time.sleep(2)
    print ("Just kidding, I'm built to serve!\n\n")
elif (intro == 2):
    print ("Welcome dino! How can I help?\n\n")
elif (intro == 3):
    print ("I'm programmed to obey the three laws of robotics. I always forget what they are though.\n\n")
elif (intro == 4):
    print ("Guess you're not as clever as you thought if you need me to do all this maths.\n")
else:
    print ("Well... that didn't work as well as I thought.\n\n")

print ("---\n")
Globals.Globals()

with open("comments_replied_to.txt", "r") as f:
    comments_replied_to = f.read()
    comments_replied_to = comments_replied_to.split("\n")
    comments_replied_to = list(filter(None, comments_replied_to))
subreddit = reddit.subreddit('CenturyofBlood+CenturyofBloodMods+COBEventsTeam')
for comment in subreddit.stream.comments(skip_existing=False):
    comment.refresh()
    if(re.search('/u/maesterbot' or 'u/maesterbot',comment.body,re.IGNORECASE) and comment.id not in comments_replied_to): #Make sure we're tagged in order to run. Non caps-sensitive.
        comments_replied_to.append(comment.id)



        if(re.search("Roll Baby",comment.body,re.IGNORECASE)):
            roundmessage = ""
            outcome = ""
            multiplesRoll = 0
            complicationRoll = 0
            sexRoll2 = 0
            sexRoll3 = 0
            generalRoll = random.randint(1,1000)
            print("Rolling Baby\n---\n")
            
            if(generalRoll < 31):
                outcome = "Twins/Multiples"
                multiplesRoll = random.randint(1,1000)
                complicationRoll = random.randint(1,10)
                
            elif(generalRoll <= 796):
                outcome = "Single Child that survives"

            elif(generalRoll <= 897):
                outcome = "Single Child that survives, mother has a complication"
                complicationRoll = random.randint(1,10)

            elif(generalRoll <= 968):
                outcome = "Single Child dies, mother survives"
                complicationRoll = random.randint(1,10)

            elif(generalRoll <= 985):
                outcome = "Single Child survives, mother dies"

            else:
                outcome = "Mother and Child die"

            roundmessage += "General Roll: **{}**\n\n".format(generalRoll)
            roundmessage += "**{}**\n\n ***\n\n".format(outcome)

            if(multiplesRoll != 0):
                if(multiplesRoll <= 25):
                    outcome = "Mother dies, twins survive"
                elif(muliplesRoll <= 40):
                    outcome = "Mother dies, one twin dies while the other survives"
                elif(muliplesRoll <= 45):
                    outcome = "Mother and both twins die"
                elif(muliplesRoll <= 156):
                    outcome = "One twin dies"
                elif(muliplesRoll <= 175):
                    outcome = "Both twins die"
                elif(muliplesRoll <= 892):
                    outcome = "Fraternal twins that survive"
                    sexRoll2 = random.randint(1,2)
                elif(muliplesRoll <= 996):
                    outcome = "Identical twins that survive"
                else:
                    outcome = "Triplets!"
                    sexRoll2 = random.randint(1,2)
                    sexRoll3 = random.randint(1,2)

                roundmessage += "Multiples Roll: **{}**\n\n".format(multiplesRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)

            if(complicationRoll != 0):
                if(complicationRoll <= 3):
                    outcome = "Mother's complication does not affect future fertility"
                elif(complicationRoll <= 6):
                    outcome = "Mother's future fertility is decreased"
                elif(complicationRoll <= 8):
                    outcome = "Mother's chance of future stillbirths/miscarriages/maternal death is increased"
                else:
                    outcome = "Mother is infertile in the future"
                roundmessage += "Complication Roll: **{}**\n\n".format(complicationRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)

            sexRoll = random.randint(1,2)
            if(sexRoll == 1):
                outcome = "Male Child"
            else:
                outcome = "Female Child"
                
            roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll)
            roundmessage += "**{}**\n\n".format(outcome)

            if (sexRoll2 != 0):
                if(sexRoll2 == 1):
                    outcome = "Male Child"
                else:
                    outcome = "Female Child"
                roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll2)
                roundmessage += "**{}**\n\n".format(outcome)
                if (sexRoll3 != 0):
                    if(sexRoll3 == 1):
                        outcome = "Male Child"
                    else:
                        outcome = "Female Child"
                    roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll3)
                    roundmessage += "**{}**\n\n".format(outcome)
                    
            roundmessage += "***\n\n"

            comment.reply(roundmessage)#Post all at once
            with open("comments_replied_to.txt", "w") as f:
                for comment_id in comments_replied_to:
                    f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



        elif(re.search("Roll Traits",comment.body,re.IGNORECASE)):
            roundmessage = ""
            outcome = ""
            goodRoll = 0
            goodRoll2 = 0
            goodRoll3 = 0
            badRoll = 0
            badRoll2 = 0
            badRoll3 = 0
            genius = False
            beautiful = False
            strong = False
            generalRoll = random.randint(1,10)
            print("Rolling Traits")
            

            if(generalRoll == 1):
                outcome = "Child has a good/neutral characteristic"
                goodRoll = random.randint(1,1000)

            elif(generalRoll == 2):
                outcome = "Child has a bad/harmful characteristic"
                badRoll = random.randint(1,1000)

            elif(generalRoll == 3):
                outcome = "Child has both a good and bad characteristic"
                goodRoll = random.randint(1,1000)
                badRoll = random.randint(1,1000)

            else:
                outcome = "Child has no outstanding characteristics at birth"

            roundmessage += "Characteristic Roll: **{}**\n\n".format(generalRoll)
            roundmessage += "**{}**\n\n ***\n\n".format(outcome)


            if(goodRoll != 0):
                if(goodRoll <= 24):
                    outcome = "Child has a genius intellect, or is gifted in a particular field"
                    genius = True
                    roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                elif(goodRoll <= 34):
                    outcome = "Child is especially attractive/beautiful"
                    beautiful = True
                    roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                elif(goodRoll <= 56):
                    outcome = "Child has a large size/height"
                    roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                elif(goodRoll <= 88):
                    outcome = "Child is especially physically strong"
                    strong = True
                    roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                elif(goodRoll <= 94):
                    outcome = "Child is on the LGBTQ spectrum"
                    roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll)
                    roundmessage += "**{}**\n\n ***\n\n".format(outcome)
                else:
                    
                    outcome = "Multiple good/neutral characteristics"
                    goodRoll2 = random.randint(1,94)
                    if(goodRoll2 <= 24):
                        outcome = "Child has a genius intellect, or is gifted in a particular field"
                        genius = True
                        goodRoll3 = random.randint(25,94)
                        if(goodRoll2 <= 34):
                            outcome2 = "Child is especially attractive/beautiful"
                            beautiful = True
                        elif(goodRoll2 <= 56):
                            outcome2 = "Child has a large size/height"
                        elif(goodRoll2 <= 88):
                            outcome2 = "Child is especially physically strong"
                            strong = True
                        else:
                            outcome = "Child is on the LGBTQ spectrum"
                            
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll2)
                        roundmessage += "**{}**\n\n".format(outcome)
                        roundmessage += "Good/Neutral Characteristic Roll: **{}**\n\n".format(goodRoll3)
                        roundmessage += "**{}**\n\n ***\n\n".format(outcome2)
                        
                    elif(goodRoll2 <= 34):
                        outcome = "Child is especially attractive/beautiful"
                        beautiful = True
                    elif(goodRoll2 <= 56):
                        outcome = "Child has a large size/height"
                    elif(goodRoll2 <= 88):
                        outcome = "Child is especially physically strong"
                        strong = True
                    else:
                        outcome = "Child is on the LGBTQ spectrum"
                    
                    
            

            if(multiplesRoll != 0):
                if(multiplesRoll <= 25):
                    outcome = "Mother dies, twins survive"
                elif(muliplesRoll <= 40):
                    outcome = "Mother dies, one twin dies while the other survives"
                elif(muliplesRoll <= 45):
                    outcome = "Mother and both twins die"
                elif(muliplesRoll <= 156):
                    outcome = "One twin dies"
                elif(muliplesRoll <= 175):
                    outcome = "Both twins die"
                elif(muliplesRoll <= 892):
                    outcome = "Fraternal twins that survive"
                    sexRoll2 = random.randint(1,2)
                elif(muliplesRoll <= 996):
                    outcome = "Identical twins that survive"
                else:
                    outcome = "Triplets!"
                    sexRoll2 = random.randint(1,2)
                    sexRoll3 = random.randint(1,2)

                roundmessage += "Multiples Roll: **{}**\n\n".format(multiplesRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)

            if(complicationRoll != 0):
                if(complicationRoll <= 3):
                    outcome = "Mother's complication does not affect future fertility"
                elif(complicationRoll <= 6):
                    outcome = "Mother's future fertility is decreased"
                elif(complicationRoll <= 8):
                    outcome = "Mother's chance of future stillbirths/miscarriages/maternal death is increased"
                else:
                    outcome = "Mother is infertile in the future"
                roundmessage += "Complication Roll: **{}**\n\n".format(complicationRoll)
                roundmessage += "**{}**\n\n ***\n\n".format(outcome)

            sexRoll = random.randint(1,2)
            if(sexRoll == 1):
                outcome = "Male Child"
            else:
                outcome = "Female Child"
                
            roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll)
            roundmessage += "**{}**\n\n".format(outcome)

            if (sexRoll2 != 0):
                if(sexRoll2 == 1):
                    outcome = "Male Child"
                else:
                    outcome = "Female Child"
                roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll2)
                roundmessage += "**{}**\n\n".format(outcome)
                if (sexRoll3 != 0):
                    if(sexRoll3 == 1):
                        outcome = "Male Child"
                    else:
                        outcome = "Female Child"
                    roundmessage += "Sex Roll: **{}**\n\n".format(sexRoll3)
                    roundmessage += "**{}**\n\n".format(outcome)
                    
            roundmessage += "***\n\n"

            comment.reply(roundmessage)#Post all at once
            with open("comments_replied_to.txt", "w") as f:
                for comment_id in comments_replied_to:
                    f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.


            
        elif(re.search("Roll",comment.body,re.IGNORECASE)):
            battleInfo = re.findall("(\d+)([d])(\d+)([\+\-]?\d*)(.*)",comment.body)
            if(battleInfo):
                roundmessage= ""
                for j in battleInfo:
                    bonus = 0
                    noDice = int(j[0]) #(battleInfo.group(1))
                    sizeDice = int(j[2]) #(battleInfo.group(3))
                    if (j[3]):
                        bonus = int(j[3]) #(battleInfo.group(4))
                    else:
                        bonus = 0
                    name = j[4] #battleInfo.group(5)
                    number = 0
                    printedBonus = 0
                    numberBonus = 0
                    runningBonus = "("
        
                    while(noDice != number):
                        printed = random.randint(1,sizeDice)
                        printedBonus += printed
                        print("Rolling ", name, "\n")
                        if (noDice - number == 1):
                            runningBonus += "{})".format(printed)
                        else:
                            runningBonus += "{} + ".format(printed)
                        number += 1
                        
                    printedBonus += bonus
                        
                    if (bonus > 0):
                        roundmessage += "{}d{}+{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                        roundmessage += "\n\n {} + {} \n\n *** \n\n".format(runningBonus,bonus)
                    elif (bonus < 0):
                        roundmessage += "{}d{}-{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                        roundmessage += "\n\n {} {} \n\n *** \n\n".format(runningBonus,bonus)
                    elif (noDice > 1):
                        roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                        roundmessage += "\n\n {} \n\n *** \n\n".format(runningBonus)
                    else:
                        roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                        roundmessage += "\n\n *** \n\n"

                comment.reply(roundmessage)#Post all at once
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
                print("---\n")
          
            else:
                print ("Improperly formatted roll\n---\n")
                comment.reply("Improperly formatted Roll. Please format comment as follows: \n \n 1d100 \n \n Roll \n \n tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Archery",comment.body,re.IGNORECASE)):
            battleInfo = re.findall("(.*)([\+\-]?\d*)",comment.body)
            if(battleInfo):
                archerymessage = "#Archery Contest"
                archerymessage += "*I am a bot by dino. Please upvote my comments so I can respond quicker and run faster.* \n \n"
                archerymessage += "--- \n \n"
                roundmessage = ""
                step = 1
                roundover = 7
                for step in roundover:
                    roundmessage+="##Round {}".format(step)
                    for j in battleInfo:
                        bonus = 0
                        name = j[0]
                        printed = random.randint(1,100)
                        if (j[1]):
                            bonus = int(j[1]) #(battleInfo.group(4))
                            printedBonus = printed + bonus
                            if (printedBonus >100):
                                printedBonus = 100
                            roundmessage += "{}: **{}**".format(name,)
                            roundmessage += "\n\n ({} + {}): {} \n\n *** \n\n".format(printed,bonus,printedBonus)
                        else:
                            bonus = 0

                        printed = random.randint(1,100)
                        

                        roundmessage += "{}d{}+{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                        roundmessage += "\n\n {} + {} \n\n *** \n\n".format(runningBonus,bonus)
                        number = 0
                        printedBonus = 0
                        numberBonus = 0
                        runningBonus = "("
            
                        while(noDice != number):
                            printed = random.randint(1,sizeDice)
                            printedBonus += printed
                            print(name)
                            if (noDice - number == 1):
                                runningBonus += "{})".format(printed)
                            else:
                                runningBonus += "{} + ".format(printed)
                            number += 1
                            
                        printedBonus += bonus
                            
                        if (bonus > 0):
                            roundmessage += "{}d{}+{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                            roundmessage += "\n\n {} + {} \n\n *** \n\n".format(runningBonus,bonus)
                        elif (bonus < 0):
                            roundmessage += "{}d{}-{} {}: **{}**".format(noDice,sizeDice,bonus,name,printedBonus)
                            roundmessage += "\n\n {} {} \n\n *** \n\n".format(runningBonus,bonus)
                        elif (noDice > 1):
                            roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                            roundmessage += "\n\n {} \n\n *** \n\n".format(runningBonus)
                        else:
                            roundmessage += "{}d{} {}: **{}**".format(noDice,sizeDice,name,printedBonus)
                            roundmessage += "\n\n *** \n\n"

                comment.reply(roundmessage)#Post all at once
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")

          
            else:
                print ("Improperly formatted roll")
                comment.reply("Improperly formatted Roll. Please format comment as follows: \n \n 1d100 \n \n Roll \n \n tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.

            
        elif(re.search("Naval Battle",comment.body,re.IGNORECASE)):
            Globals.battleType = "Naval"
            battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
            if(battleInfo):
                print ("Running Naval battle\n")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in battle.run(battleInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(60)
                else:
                    print ("Quick Mode\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")

                print("---\n")
            else:
                print ("Improperly formatted battle\n---\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



                    
        elif(re.search("Land Battle",comment.body,re.IGNORECASE)):
            Globals.battleType = "Land"
            battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
            if(battleInfo):
                print ("Running Land battle\n")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in battle.run(battleInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(60)
                else:
                    print ("Quick Mode\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                print("---\n")
            else:
                print ("Improperly formatted battle\n---\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Ambush",comment.body,re.IGNORECASE)):
            Globals.battleType = "Ambush"
            battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
            if(battleInfo):
                print ("Running Ambush battle\n")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in battle.run(battleInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(60)
                else:
                    print ("Quick Mode\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                print("\n---\n")
            else:
                print ("Improperly formatted battle\n---\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



        elif(re.search("Assault",comment.body,re.IGNORECASE)):
            Globals.battleType = "Assault"
            battleInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)\n+(.*) (\d+) ([\+\-]?\d*)",comment.body)
            if(battleInfo):
                print ("Running Assault")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in battle.run(battleInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(60)
                else:
                    print ("Quick Mode\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                print("---\n")
            else:
                print ("Improperly formatted battle\n---\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows: \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Blunted Duel",comment.body,re.IGNORECASE)):
            Globals.battleType = "Blunted"
            duelInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)",comment.body)
            if(duelInfo):
                print ("Running Blunted Duel\n")
                duel = Duel.Duel()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in duel.run(duelInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(30)
                    
                elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                    Globals.resultsMode = True
                    print ("Results Mode\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                else:
                    Globals.resultsMode = False
                    print ("Quick Mode\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                print("---\n")
            else:
                print ("Improperly formatted duel\n---\n")
                comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Live Duel",comment.body,re.IGNORECASE)):
            Globals.battleType = "Live"
            duelInfo = re.match("(.*) ([\+\-]?\d*)\n+(.*) ([\+\-]?\d*)",comment.body)
            if(duelInfo):
                print ("Running Live Duel\n")
                duel = Duel.Duel()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in duel.run(duelInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(30)
                    
                elif(re.search("Results Mode",comment.body,re.IGNORECASE)):
                    Globals.resultsMode = True
                    print ("Results Mode\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                else:
                    Globals.resultsMode = False
                    print ("Quick Mode\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")

                print("--- \n")
            else:
                print ("\nImproperly formatted duel\n--- \n")
                comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n\ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.



        elif(re.search("Boxing",comment.body,re.IGNORECASE)):
            duelInfo = re.match("(.*) (\d*)\n+(.*) (\d*)",comment.body)
            if(duelInfo):
                print ("Running Boxing Match\n")
                box = Boxing.Boxing()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic Mode\n")
                    lastcomment = comment
                    comments_replied_to.append(lastcomment.id)
                    for roundCount in box.run(duelInfo).split("---"):
                        try:
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        except: #Shouldn't happen too much, but in case we get rate limited.
                            print("Rate limited. Sleeping for 6 minutes.")
                            time.sleep(360)
                            lastcomment = lastcomment.reply(roundCount)
                            comments_replied_to.append(lastcomment.id)
                            with open("comments_replied_to.txt", "w") as f:
                                for comment_id in comments_replied_to:
                                    f.write(comment_id + "\n")
                        time.sleep(30)
                else:
                    print ("Quick Mode\n")
                    comment.reply(box.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
                print("---\n")
            else:
                print ("Improperly formatted boxing match\n---\n")
                comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1  Health \n \nName of PC 2  Health \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.




        else:
            comment.reply("Improperly formatted info. Please state which function you wish to use; Roll, Land Battle, Naval Battle, Ambush, Assault, Boxing, Live Duel, or Blunted Duel")
            print("Improperly formatted info\n---\n")


