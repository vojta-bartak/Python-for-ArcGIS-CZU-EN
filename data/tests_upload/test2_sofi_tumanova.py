import os

os.chdir(r"D:\CZU\PGISRS\PR_test")

files = []
for f in os.listdir("."):
    if f[-4:] == ".txt":
        files.append(f)

out_file = open("output_table.csv", "w")
out_file.write("ID;Temp\n")


for path in files:
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    new_temp = 1

    for line in lines [:]:
         items = line.split(";")
         ID = int(items[0])
         Temp = int(items[1])
         new_temp = Temp + 273.15

    out_file.write(srt(ID) + ";" + (new_temp) + "\n")

out_file.close()
