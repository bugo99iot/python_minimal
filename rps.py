from random import randint
 
#create a list of play options
t = ["rock", "paper", "scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]

#print computer

points_player = 0
points_computer = 0

while points_computer < 3 and points_player < 3:
#set player to True
    player = raw_input("Rock, Paper, Scissors?").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            points_computer += 1
        else:
            print("You win!", player, "smashes", computer)
            points_player += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            points_computer += 1
        else:
            print("You win!", player, "covers", computer)
            points_player += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            points_computer += 1
        else:
            print("You win!", player, "cut", computer)
            points_player += 1
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    #your status changes from False to True because any value assigned to the variable player makes player True
    computer = t[randint(0,2)]

print "The game is over. Final score: computer %d points, player %d points" % (points_computer, points_player)
