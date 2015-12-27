from random import shuffle
import sys

# This program is a scorecard for Speed Uno

# this gets a valid number of players
loop4NOP=1		# Added by Albert for USER EXPERIENCE
while(loop4NOP):	# Will continue looping until user inputs x for exit or valid number of players.
    numofplayers = raw_input("How many players are there? ") 
    if (str(numofplayers) == 'x' or str(numofplayers) =='X'):
        sys.exit()
    try:
        numofplayers = int(numofplayers)
    except ValueError:
        valid = 0
        while valid == 0:
            numofplayers = raw_input("Please enter a number for how many players there are.")
            try:
                numofplayers = int(numofplayers)
            except ValueError:
                valid = 0
            else:
                valid = 1

    # this exits the program if an invalid number of players is selected 
    if (numofplayers == 6 or numofplayers == 8 or numofplayers == 9 or numofplayers == 10 or numofplayers ==12 or numofplayers == 14 or numofplayers == 15):
        print "There are " + str(numofplayers) + " players."
        loop4NOP=0
    else:
        print("This is not a valid number of players. You need to have either 6, 8, 9, 10, 12, 14, or 15 people playing.")
        print("Please try again. - or enter x to exit")
    
# this determines ending score
endscore = raw_input("What score would you like to play to?")
try:
    endscore = int(endscore)
except ValueError:
    valid = 0
    while valid == 0:
        endscore = raw_input("Please enter a number for the ending score")
        try:
            endscore = int(endscore)
        except ValueError:
            valid = 0
        else:
            valid = 1
            print "The ending score is " + endscore

#this creates a list of players and records names
listofplayers = []
for i in range(1, numofplayers + 1):
    playername = raw_input("What is player " + str(i) + "'s name?")
    listofplayers.append({'name':playername, 'score':0, 'team': 0})

# determines teams for players
teamone = []
teamtwo = []
teamthree = []
print numofplayers
if numofplayers == 6:
    shuffle(listofplayers)
    for i in listofplayers[0:3:1]:
        i['team'] = 1
    for i in listofplayers[3:6:1]:
        i['team'] = 2
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
    

elif numofplayers == 8:
    shuffle(listofplayers)
    for i in listofplayers[0:4:1]:
        i['team'] = 1
    for i in listofplayers[4:8:1]:
        i['team'] = 2
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
elif numofplayers == 9:
    shuffle(listofplayers)
    for i in listofplayers[0:3:1]:
        i['team'] = 1
    for i in listofplayers[3:6:1]:
        i['team'] = 2
    for i in listofplayers[6:9:1]:
        i['team'] = 3
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
        if i['team'] == 3:
            teamthree.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
    print("Team 3: " + ', '.join(teamthree))
elif numofplayers == 10:
    shuffle(listofplayers)
    for i in listofplayers[0:5:1]:
        i['team'] = 1
    for i in listofplayers[5:10:1]:
        i['team'] = 2
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
elif numofplayers == 12:
    shuffle(listofplayers)
    for i in listofplayers[0:4:1]:
        i['team'] = 1
    for i in listofplayers[4:8:1]:
        i['team'] = 2
    for i in listofplayers[8:12:1]:
        i['team'] = 3
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
        if i['team'] == 3:
            teamthree.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
    print("Team 3: " + ', '.join(teamthree))
elif numofplayers == 14:
    shuffle(listofplayers)
    for i in listofplayers[0:7:1]:
        i['team'] = 1
    for i in listofplayers[7:14:1]:
        i['team'] = 2
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
elif numofplayers == 15:
    shuffle(listofplayers)
    for i in listofplayers[0:5:1]:
        i['team'] = 1
    for i in listofplayers[5:10:1]:
        i['team'] = 2
    for i in listofplayers[10:15:1]:
        i['team'] = 3
    for i in listofplayers:
        if i['team'] == 1:
            teamone.append(i['name'])
        if i['team'] == 2:
            teamtwo.append(i['name'])
        if i['team'] == 3:
            teamthree.append(i['name'])
    print("Team 1: " + ', '.join(teamone))
    print("Team 2: " + ', '.join(teamtwo))
    print("Team 3: " + ', '.join(teamthree))

seatorder = listofplayers
# this sets up the check to see if the game should end
endgame = 0
while endgame == 0:
    
    # this updates the scores of the players
    for i in seatorder:
        score = raw_input("What is " + i['name'] + "'s score? ")
        try:
            score = int(score)
        except ValueError:
            valid = 0
            while valid == 0:
                score = raw_input("Please enter a number for " + i['name'] + "'s score")
                try:
                    score = int(score)
                except ValueError:
                    valid = 0
                else:
                    valid = 1
        i['score'] = i['score'] + score
        print i['name'] + "'s total score is: " + str(i['score'])
        print " "
    
    # this gives the seating order of the players
    seatorder = sorted(listofplayers, key=lambda k: k['score'])
    print " "
    print " "
    print "The seating order is:"
    for i in seatorder:
        print i['name'] + " with a score of " + str(i['score'])
        
    # this checks if the game is supposed to end
    for i in seatorder:
        if i['score'] >= endscore:
            endgame = 1
            break
    if endgame == 1:
        break
    
    # this section checks if the last place person wants to guess the number of cards
    draw = 0
    for i in seatorder[numofplayers - 1:]:
        valid = 0
        while valid == 0:
            print " "
            draw = raw_input("Does " + i['name'] + " want to draw for cards? Please type 'y' or 'n': ")
            if (draw == 'y' or draw == 'Y'):
                valid = 1
                scoremod = 0
                valid2 = 0
                while valid2 == 0:
                    print " "
                    scoremod = raw_input("Was the draw correct? Please type 'y' or 'n': ")
                    if (scoremod == 'y' or scoremod == 'Y'):
                        valid2 = 1
                        i['score'] = i['score'] - 100
                        if i['score'] < 0:
                            i['score'] = 0
                        print i['name'] + "'s score is " + str(i['score'])
                    elif (scoremod == 'n' or scoremod == 'N'):
                        valid2 = 1
                        scoremod = 0
                        valid3 = 0
                        while valid3 == 0:
                            print " "
                            scoremod = raw_input("Was the draw 1 card away? Please type 'y' or 'n': ")
                            if (scoremod == 'y' or scoremod == 'Y'):
                                valid3 = 1
                                i['score'] = i['score'] + 50
                                print i['name'] + "'s score is " + str(i['score'])
                            elif (scoremod == 'n' or scoremod == 'N'):
                                valid3 = 1
                            else:
                                valid3 = 0
                    else:
                        valid2 = 0
            elif (draw == 'n' or draw == 'N'):
                valid = 1
            else:
                valid = 0
                

            
# this prints the winning team

# this part prints for games of 6, 8, or 10 players (two teams)
if (numofplayers == 6 or numofplayers == 8 or numofplayers == 10 or numofplayers == 14):
    scoreteamone = 0
    scoreteamtwo = 0
    for i in seatorder[int(numofplayers) - 4:int(numofplayers) - 1: 1]:
        if i['team'] == 1:
            scoreteamone = scoreteamone + 1
        if i['team'] == 2:
            scoreteamtwo = scoreteamtwo + 1
    if scoreteamone < scoreteamtwo:
        print " "
        print "Team one wins!"
        for i in seatorder:
            if i['team'] == 1:
                print i['name']
    else:
        print " "
        print "Team two wins!"
        for i in seatorder:
            if i['team'] == 2:
                print i['name']
    
# this part prints for games of 9 or 12 players (three teams)
if (numofplayers == 9 or numofplayers == 12 or numofplayers == 15):
    scoreteamone = 0
    scoreteamtwo = 0
    scoreteamthree = 0
    for i in seatorder[int(numofplayers) - 5:int(numofplayers) - 1: 1]:
        if i['team'] == 1:
            scoreteamone = scoreteamone + 1
        if i['team'] == 2:
            scoreteamtwo = scoreteamtwo + 1
        if i['team'] == 3:
            scoreteamthree = scoreteamthree + 1

# this section checks for ties and settles by taking lowest total score of players
    if (scoreteamone == scoreteamtwo and scoreteamone < scoreteamthree):
        totalteamone = 0
        totalteamtwo = 0
        for i in seatorder:
            if i['team'] == 1:
                totalteamone = totalteamone + i['score']
            elif i['team'] == 2:
                totalteamtwo = totalteamtwo + i['score']
        if totalteamone < totalteamtwo:
            print " "
            print "Team one wins!"
            for i in seatorder:
                if i['team'] == 1:
                    print i['name']
        else:
            print " "
            print "Team two wins!"
            for i in seatorder:
                if i['team'] == 2:
                    print i['name']
    elif (scoreteamone == scoreteamthree and scoreteamone < scoreteamtwo):
        totalteamone = 0
        totalteamthree = 0
        for i in seatorder:
            if i['team'] == 1:
                totalteamone = totalteamone + i['score']
            elif i['team'] == 3:
                totalteamthree = totalteamthree + i['score']
        if totalteamone < totalteamthree:
            print " "
            print "Team one wins!"
            for i in seatorder:
                if i['team'] == 1:
                    print i['name']
        else:
            print " "
            print "Team three wins!"
            for i in seatorder:
                if i['team'] == 3:
                    print i['name']
    elif (scoreteamtwo == scoreteamthree and scoreteamtwo < scoreteamone):
        totalteamtwo = 0
        totalteamthree = 0
        for i in seatorder:
            if i['team'] == 2:
                totalteamtwo = totalteamtwo + i['score']
            elif i['team'] == 3:
                totalteamthree = totalteamthree + i['score']
        if totalteamtwo < totalteamthree:
            print " "
            print "Team two wins!"
            for i in seatorder:
                if i['team'] == 2:
                    print i['name']
        else:
            print " "
            print "Team three wins!"
            for i in seatorder:
                if i['team'] == 3:
                    print i['name']

# this section declares winner if there are no ties
    else:
        teamscoredict = {1:scoreteamone, 2:scoreteamtwo, 3:scoreteamthree}
        winningteam = min(teamscoredict, key=teamscoredict.get)
        if winningteam == 1:
            print " "
            print "Team one wins!"
            for i in seatorder:
                if i['team'] == 1:
                    print i['name']
        elif winningteam == 2:
            print " "
            print "Team two wins!"
            for i in seatorder:
                if i['team'] == 2:
                    print i['name']
        elif winningteam == 3:
            print " "
            print "Team three wins!"
            for i in seatorder:
                if i['team'] == 3:
                    print i['name']

# this prints the final scores
print " "
print "The final scores are: "
for i in seatorder:
    print i['name'] + " from team " + str(i['team']) + " has a score of " + str(i['score'])
    
    
    
