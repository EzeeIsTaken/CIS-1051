height = int(input("height"))

while height < 1 or height > 8:
   height = int(input("height"))

def mario(height):
   for i in range(1, height+1, 1):
      print("")
      for dots in range(height-i, 0, -1):
         print(" ", end = "")
      for i in range(i):
         print("#", end = "")

mario(height)
