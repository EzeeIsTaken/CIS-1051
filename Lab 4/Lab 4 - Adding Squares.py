n = int(input("What do you want to add"))


def adding(n):
   s = 0
   for i in range(1, n+1):
      s += i**2
   print(s)

adding(n)
