import random as rn

x, y = rn.randint(1,9), rn.randint(1,9)

a = input("Calculate " + str(x) + " times " + str(y) + ": ")

yes = "yes"
no = "No"

while a != x*y:
    a = input("Wrong, try it again:")
b = input("Great, next excersise? Type Yes or No: " )

if str (yes) == "yes":
    x, y = rn.randint(1,9), rn.randint(1,9)
a = input("Calculate " + str(x) + " times " + str(y) + ": ")
while a != x*y:
    a = input("Wrong, try it again:")
b = input("Great, next excersise? Type Yes or No: " )


if b != "yes":
    print("the end, thank you!")

        
       
