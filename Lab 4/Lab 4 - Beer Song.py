def beerSong(n):
   for i in range(n):
      print(n, "bottles of beer on the wall,", n, "bottles of beer \n", 
      "Take one down, pass it around,", n-1, "bottles of beer on the wall")
      n -= 1

beers = int(input("How many beers are on the wall?"))
beerSong(beers)
