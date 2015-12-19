from random import shuffle

# This program is a scorecard for Speed Uno

# this gets a valid number of players
numofplayers = raw_input("How many players are there?")
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
            print "There are " + str(numofplayers) + " players."
else:
    print "There are " + str(numofplayers) + " players."
    
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
else:
    print("This is not a valid number of players")
    

# this sets up the check to see if the game should end
endgame = 0
while endgame == 0:
    
    # this updates the scores of the players
    for i in listofplayers:
        score = raw_input("What is " + i['name'] + "'s score?")
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
    
    # this gives the seating order of the players
    seatorder = sorted(listofplayers, key=lambda k: k['score'])
    for i in seatorder:
        print i['name']
        
    # this checks if the game is supposed to end
    for i in seatorder:
        if i['score'] >= endscore:
            endgame = 1
# this prints the winning team            

# this prints the final scores
for i in seatorder:
    print i['name'] + " has a score of " + str(i['score'])
    
    
    