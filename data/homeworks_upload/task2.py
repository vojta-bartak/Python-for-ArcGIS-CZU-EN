import random
import random as rn
a=random.randint(1,5)
print(a)
b=random.randint(1,5)
print(b)
real_result=a*b
c=input("the result of the multiplication is:")
while c!=real_result:
    print("try again man")
    c= input("the n result of the multiplication is:")
else:
    print("well done man it is",c)
