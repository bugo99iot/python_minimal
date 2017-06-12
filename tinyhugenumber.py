number =  input("Give me a number bewtween 1 and 20: ")
#watch out, raw_input takes converts your entry into a string
#you could also do: number = int(input("Enter a number: ")), wchich converts entered string into an integer
print "your input was", number
check = number *2
print "yes! ", "two times ", number, "is", check, ".", number, "is a number!"
#

while number <0 or number > 20:
    print "Your number is not in the selected range"
    number =  input("Give me a number bewtween 1 and 10: ")

if number >= 11:
    print "wow such a huge number!"
else:
    print "? why such a tiny one?"

