import time, threading

fr = raw_input("What do you think? I the world flat or round? Write your answer here: ").lower()

def repeatf():
    print "The world is flat!"
    threading.Timer(1, repeatf).start()

def repeatr():
    print "The world is round!"
    threading.Timer(1, repeatr).start()

while fr != "flat" and fr != "round":
    fr = raw_input("You didn't choose flat or round. What do you think? Is the world flat or round? Write your answer here: ").lower()

if fr == "flat":
    print "You are right!"
    repeatf()
else:
    print "You are right!"
    repeatr()

