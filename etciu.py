print "ETCIU!"

yesno = raw_input("Did you sneeze? ").lower()

while yesno != "yes" and yesno != "y" and yesno != "no" and yesno != "n":
    print "Sorry, you have to say yes or no."
    yesno = raw_input("Did you sneeze? ").lower()

if yesno == "yes" or yesno == "y":
    print "..."
    print "..."
    print "BLESS YOU!"
else:
    print "..."
    print "..."
    print "Sorry, I thought you sneezed."

