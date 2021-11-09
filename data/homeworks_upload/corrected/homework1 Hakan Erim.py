a     = [12,0,39,50,1]
b    = len(a)
new_a = []
i     = 0

while i < b:
    mini = min(a)      
    new_a.append(mini) 
    a.remove(mini)     
    i += 1      
print(new_a)
