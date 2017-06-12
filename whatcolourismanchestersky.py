colour = raw_input("What colour is Manchester sky? Type your colour here: ").lower()

while colour != "grey":
    if colour == "blue":
        print colour, "?", " Naaaa, you are dreaming. But super close."
    elif colour == "green":
        print "Green like the leaves? Sorry, not for today, try again!"
    elif colour == "red":
        print colour, "?", " Perhaps at the sunset? Not really. One more try."
    elif colour == "black":
        print "Really? In the middle of the night? Not at all. We need to make some progress here."       
    else:
        print colour, "?", "Oh, you were so close! You need to give it one more chance."

    colour = raw_input("What colour is Manchester sky? Type your colour here: ").lower()

print "Yeah, you are right!"
print "You guessed it!"
print "It's pretty grey!"
