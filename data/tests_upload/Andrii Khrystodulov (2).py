# Find all the divisors

m = 1111
list = range(1, 1112)


for i in list:
  if m % i == 0:
    print('Here are all division numbers: ')
    print(i)


