import random


# B B B B B R R

def game():
   deck = ["B"] * 5 + ["R"] * 2
   random.shuffle(deck)
   picks = []
   while len(picks) < 3:
      p = random.randint(0,6)
      if p not in picks:
         picks.append(p)
   chosenCards = []
   for p in picks:
      chosenCards.append(deck[p])
   #print(chosenCards)
   if "R" in chosenCards:
      return False
   else:
      return True

TRIALS = 10000
wins = 0

for _ in range(TRIALS):
   if game() == True:
      wins += 1
print(wins/TRIALS)
   
   

