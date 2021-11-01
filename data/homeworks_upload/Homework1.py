import random as rn
x,y= rn.randint(1,9), rn.randint(1,9)
a= input(" Calculate " + str(x) + " times " + str(y) + " : ")
while a!=x*y:
    a=input(" wrong, try again: ")
b=input(" great, do you want new challenge " " (yes/no(please write with quotation mark)) : ")
if str(b)==" yes ":
    x,y=rn.randint(1,9), rn.randint(1,9)
a=input (" Calculate " + str(x) + " times " + str(y) + " : ")
while a!=x*y:
    a=input (" wrong, try again: ")
b=input(" great, do you want new challenge " " (yes/no(please write with quotation mark)) : ")
if b!=" yes ":
    print(" see you ")
