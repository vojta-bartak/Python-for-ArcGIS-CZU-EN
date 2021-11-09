import os
os.chdir(r"C:\Users\xerih002.CZU\Desktop\test")

files=os.listdir


out_file= open("output_table.csv", "w")
out_file.write("STAID; Temperature\n")

for path in files:
    
   f= open(path,"r")
   lines=f.readlines()
   f.close()

total_t += float(temp)/10
count_t += 1

temp= total_t + 273




out_file.write(str(STAID)+ ";" + str(Temperature) + "\n")
out_file.close()
