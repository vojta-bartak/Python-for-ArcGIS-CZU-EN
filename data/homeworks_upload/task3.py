import random
import random as rn
a=random.randint(1,5)
print(a)
b=random.randint(1,5)
print(b)
real_result=a*b
c=input("the result of the multiplication is:")
while c!=real_result:
    print("try again baby")
    c= input("the n result of the multiplication is:")
else:
    print("well done baby it is",c)
    
g=input("Would you like another challenge baby?:").lower()
answers=['yes','no']
if g==answers[0]:
    c=input("the result of the multiplication is:")
    while c!=real_result:
        print("try again baby")
        t= input("the n result of the multiplication is:")
    else:
            print("well done baby it is",c)
else:
    pass



