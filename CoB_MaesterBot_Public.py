import praw
import re
import Battle
import Duel
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
    print ("Guess you're not as clever as you thought if you need me to do all this maths.\n\n")
else:
    print ("Well... that didn't work as well as I thought.\n\n")

Globals.Globals()

with open("comments_replied_to.txt", "r") as f:
    comments_replied_to = f.read()
    comments_replied_to = comments_replied_to.split("\n")
    comments_replied_to = list(filter(None, comments_replied_to))
subreddit = reddit.subreddit('CenturyofBlood+CenturyofBloodMods')
for comment in subreddit.stream.comments(skip_existing=False):
    comment.refresh()
    if(re.search('/u/maesterbot',comment.body,re.IGNORECASE) and comment.id not in comments_replied_to): #Make sure we're tagged in order to run. Non caps-sensitive.
        comments_replied_to.append(comment.id)


        if(re.search("Roll",comment.body,re.IGNORECASE)):
            Globals.battleType = "Naval"
            battleInfo = re.findall("(\d+)([d])(\d+)([\+\-]?\d*)(.*)",comment.body)
            if(battleInfo):
                roundmessage= ""
                for j in battleInfo:
                    print ("Rolling\n\n")
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
                        print(noDice)
                        print(sizeDice)
                        print(bonus)
                        print(name)
                        print(printed)
                        print(printedBonus)
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
                        roundmessage += "\n\n {} - {} \n\n *** \n\n".format(runningBonus,bonus)
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
                comment.reply("Improperly formatted Roll. Please format comment as follows (The dice you're rolling must have 3 digits, and the number of dice must have 2 e.g. 010 and 02) : \n \n Roll \n \n 01d100 \n \n tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



            
        elif(re.search("Naval Battle",comment.body,re.IGNORECASE)):
            Globals.battleType = "Naval"
            battleInfo = re.match("(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)\n+(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)",comment.body)
            if(battleInfo):
                print ("Running Naval battle")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted battle")
                comment.reply("Improperly formatted battle info. Please format comment as follows (Strength must have 4 digits, and bonus must have 2 e.g. 0100 and 02): \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



                    
        elif(re.search("Land Battle",comment.body,re.IGNORECASE)):
            Globals.battleType = "Land"
            battleInfo = re.match("(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)\n+(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)",comment.body)
            if(battleInfo):
                print ("Running Land battle")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted battle\n\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows (Strength must have 4 digits, and bonus must have 2 e.g. 0100 and 02): \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Ambush",comment.body,re.IGNORECASE)):
            Globals.battleType = "Ambush"
            battleInfo = re.match("(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)\n+(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)",comment.body)
            if(battleInfo):
                print ("Running Ambush battle")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted battle\n\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows (Strength must have 4 digits, and bonus must have 2 e.g. 0100 and 02): \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.



        elif(re.search("Assault",comment.body,re.IGNORECASE)):
            Globals.battleType = "Assault"
            battleInfo = re.match("(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)\n+(.*) ([\+\-]\d)\n+(.*) (\d\d\d\d) ([\+\-]\d\d)",comment.body)
            if(battleInfo):
                print ("Running Assault")
                battle = Battle.Battle()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(battle.run(battleInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted battle\n\n")
                comment.reply("Improperly formatted battle info. Please format comment as follows (Strength must have 4 digits, and bonus must have 2 e.g. 0100 and 02): \n \nCommanderName + CommanderBonus\n \nAttackerName AttackerStrength +AttackerBonus \n \nCommanderName + CommanderBonus\n \nDefenderName DefenderStrength +DefenderBonus\n \nDramatic Mode (optional) \n \tag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each battle so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Blunted Duel",comment.body,re.IGNORECASE)):
            Globals.battleType = "Blunted"
            duelInfo = re.match("(.*) ([\+\-]?\d+)\n+(.*) ([\+\-]?\d+)",comment.body)
            if(duelInfo):
                print ("Running Blunted Duel")
                duel = Duel.Duel()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted duel\n\n")
                comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n \ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.




        elif(re.search("Live Duel",comment.body,re.IGNORECASE)):
            Globals.battleType = "Live"
            duelInfo = re.match("(.*) ([\+\-]?\d+)\n+(.*) ([\+\-]?\d+)",comment.body)
            if(duelInfo):
                print ("Running Live Duel")
                duel = Duel.Duel()
                if(re.search("Dramatic Mode",comment.body,re.IGNORECASE)):
                    print ("Dramatic")
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
                    print ("Done\n\n")
                else:
                    print ("Boring\n\n")
                    comment.reply(duel.run(duelInfo))#Post all at once
                    with open("comments_replied_to.txt", "w") as f:
                        for comment_id in comments_replied_to:
                            f.write(comment_id + "\n")
            else:
                print ("Improperly formatted duel\n\n")
                comment.reply("Improperly formatted duel info. Please format comment as follows: \n \nName of PC 1 +X \n \nName of PC 2 +X \n \nDramatic Mode (optional) \n \n Live Duel or Blunted Duel \n\ntag MaesterBot")
                with open("comments_replied_to.txt", "w") as f:
                    for comment_id in comments_replied_to:
                        f.write(comment_id + "\n")
            time.sleep(60) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.


        else:
            comment.reply("Improperly formatted info. Please state which function you wish to use, Land Battle, Naval Battle, Ambush, Assault, Live Duel, or Blunted Duel")


