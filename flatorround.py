import time, threading
from random import randint



def repeat():
    n = randint(1,2)
    if n == 1:
        print "The world is round!"
    else:
        print "The world is flat!"
    threading.Timer(1, repeat).start()

repeat()


#def repeat():
#    print "The world is round!"
#    threading.Timer(1, repeat).start()

#repeat()
