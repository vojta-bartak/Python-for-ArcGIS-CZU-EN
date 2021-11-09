import os

os.chdir(r"C:\Users\xcvio001\Desktop\Ostoja")

allfiles=os.listdir(".")
files = []
for f in files:
    if f[-4:] == ".txt":
        files.append(f)

out_file = open("out_table.csv", "w")
out_file.write("ID;Temp\n")

for path in files:
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    items = line.split(".")
    ID = items[0]
