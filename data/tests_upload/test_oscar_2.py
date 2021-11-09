import os

os.chdir(r"C:\Users\xmaro019\Dokumenty")

# open (create) the output file
out_file = open("temperatures_kelvin.csv", "w")
out_file.write("ID;Temp\n")

#opening file
f = open("temperatures.csv", "r")

#reading temperature
lines = f.readlines()
f.close()

for line in lines[1:]:
    # separating columns
    items = line.split(";")
    tid = items[0]
    temp = items[1]

    #equation for celcius to kelvin
    kelvin = float(temp) + 273.15


    #writing files
    out_file.write(tid + ";" + kelvin + "\n")

#closing the file
out_file.close()
