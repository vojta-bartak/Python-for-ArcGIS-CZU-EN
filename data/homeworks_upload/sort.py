lit=[9,3,8,1]
for i in range(len(lit)-1):
    if  lit[i]<lit[i+1]:
        lit[i+1],lit[i]=lit[i],lit[i+1]
print(lit)
