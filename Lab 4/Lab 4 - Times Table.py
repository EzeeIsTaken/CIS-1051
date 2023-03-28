num = int(input("Give a number for the multiplication table"))
tableNum = 0
addition = 0
line = ""

for i in range(num):
   addition += 1
   tableNum = 0
   line= ""
   for j in range(num):
      tableNum += addition
      line += str(tableNum) + "\t"
   print(line)
