#this code offers the user three attempts to guess where is bassot. 
#if the user doesn't guess the location of bassot in the first n attampts, the computer offers the solution
#locations are: in the sock box, in the bathtub, having a walk, seeing his friend, chilling on the beach, with Ida at the shop

from random import randint
import sys

places = ["in the sock box", "in the bath tub", "having a walk", "seeing his friend", "at the hub", "chilling on the beach", "with ida at the shop"]

place = places[randint(0,len(places)-1)]

att_initial = int(5)

print "COMPUTER: Guess where is bassott. You have", att_initial, "attempts." 

print "Here is a list of possible places:"

for plc in places:
    print(plc)

guess = raw_input("USER: ").lower()

attempt = int(0)

while attempt < 4:
    if guess == place:
        print "You got it, bassott is", place, "!"
        print "You needed only", attempt + 1, "attempts!"
        sys.exit(0)
    else:
        print "Sorry you didn't get it. Can you guess where is bassott again?", "You have", att_initial -1  - attempt, "trials left."
        guess = raw_input("USER:").lower()
        attempt += 1
print "Sorry, you didn't get it. Bassot is %s." % (place)

#break closes the given loop and moves to the next statement, sys.exit aborts the code there
