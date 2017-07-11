#This is a code inspired by the short story 'Pushkin and Gogol', by Daniil Kharms
#If you like to read the whole story:http://absurdist.obook.org/kharms/display.php?p=37
#Daniil Kharms was a Soviet-era surrealist and absurdist short story writer and essayist
#If you like to know more about him: http://russiapedia.rt.com/prominent-russians/literature/daniil-kharms/

from random import randint
import time, threading
import sys

exclamations = ["What the devil!", "What a vile abomination! You can't even have a rest.", "Not a minute's peace!", "Always an obstacle in everything!", "Hooliganism! Sheer hooliganism!", "It's sheer mockery!", "What the devil! Well, really, what the devil!", "Vile abomination!", "What the devil!"]
gogol_excl = ["Seems I've stumbled over Pushkin!", "It's a vile abomination! Tripped over Pushkin again!", "Tripped over Pushkin again! ", "Over Pushkin!", "Over Pushkin!"]
pushkin_excl= ["Seems I've tripped over Gogol!", "What the devil! Seems I've tripped over Gogol again!", "Tripped over Gogol again!", "Over Gogol!", "Over Gogol!"]



def random_excl():
    while True:
        random_excl = exclamations[randint(0,len(exclamations)-1)]
        return random_excl

def random_gogol():
    while True:
        random_gogol = gogol_excl[randint(0,len(gogol_excl)-1)]
        return random_gogol

def random_pushkin():
    while True:
        random_pushkin = pushkin_excl[randint(0,len(pushkin_excl)-1)]
        return random_pushkin

print
print "CODED SHORT STORY SERIES: 'PUSHKIN AND GOGOL'"
print "by Daniil Kharms"
time.sleep(6)
print
print
print "GOGOL falls out from the wings on to the stage and quietly lies there."
print
time.sleep(6)
print "PUSHKIN appears on stage, stumbles over GOGOL and falls."
print
time.sleep(6)
print "PUSHKIN: What the devil! Seems I've tripped over Gogol!"
print
time.sleep(6)

i = 0
while True:
    if i % 2 == 0:
        print "GOGOL (Getting up): ", random_excl(), "(Walks off, stumbles over PUSHKIN and falls)", random_gogol()
        print
        time.sleep(6) 
        i+=1
    else:
        print "PUSKIN (Getting up): ", random_excl(), "(Walks off, stumbles over GOGOL and falls)", random_pushkin()
        print
        time.sleep(6) 
        i+=1


