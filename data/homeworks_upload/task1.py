import random
import random as rn
a=random.randint(1,5)
print(a)
b=random.randint(1,5)
print(b)
real_result=a*b
d=input("the result of the multiplication is:")
if d == real_result:
    print("congratulations, u did it man")
else:
    print("Nop, the result is",real_result,"man")
