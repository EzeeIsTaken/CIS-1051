"""
def happyDay(n):
   for i in range(n):
      print("Happy Birthday!")

bDay = int(input("How many Happy Birthdays would you like?"))
happyDay(bDay)
"""


#Part 1.1
"""
def beerSong(n):
   for i in range(n):
      print(n, "bottles of beer on the wall,", n, "bottles of beer \n", 
      "Take one down, pass it around,", n-1, "bottles of beer on the wall")
      n -= 1

beers = int(input("How many beers are on the wall?"))
beerSong(beers)
"""


#Part 1.2
"""
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
"""
"""
for i in range(1, num+1):
   for j in range(1, num+1):
      z = i*j
      print(z, end ='\t')
   print()
"""


#Part 1.3
n = int(input("What do you want to add"))


def adding(n):
   s = 0
   for i in range(1, n+1):
      s += i**2
   print(s)

adding(n)
   
