import os
os.chdir(r"C:\Users\vojta\ownCloud\Python")
#create output file
out_file=open("tempinkelvin.csv","w")
out_file.write("ID;TemperatureinKelvin\n")
#open our file
f=open("temperatures.csv","r")
lines=f.readlines()
f.close()
for line in lines[2:]:
    items=line.split(";")
    staid=int(items[0])
    temp=items[1]
#compute the new temp
    tempK=float(temp)*274.15

#write the result to the output file
    out_file.write(str(staid)+";"+str(tempK)+"\n")
out_file.close()


    
