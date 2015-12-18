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

#this creates a list of players and records names
listofplayers = []
for i in range(1, numofplayers + 1):
    playername = raw_input("What is player " + str(i) + "'s name?")
    listofplayers.append({'name':playername, 'score':0})

# this sets up the check to see if the game should end
endgame = 0
while endgame == 0:
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