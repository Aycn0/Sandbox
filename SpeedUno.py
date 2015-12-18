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
    listofplayers.append({raw_input("What is player " + str(i) + "'s name?"):0})
for i in listofplayers:
    print i
