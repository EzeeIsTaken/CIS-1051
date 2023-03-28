import random

def holdAt20(limit=20):
   turnTotal = 0
   while turnTotal < limit:
      roll = random.randint(1,6)
      #print("Roll:", roll)
      if roll == 1:
         turnTotal = 0
         #print("Turn Total:", turnTotal)
         return turnTotal
      else:
         turnTotal += roll
   #print("Turn Total:", turnTotal)
   return turnTotal

def holdAt20Outcomes(trials):
   outcomes = {0:0}
   for value in range(20,26):
      outcomes[value] = 0

   for _ in range(trials):
      score = holdAt20()
      outcomes[score] += 1


   for score in outcomes:
      print(score, outcomes[score]/trials)

def holdAtXOutcomes(trials, limit):
   outcomes = {0:0}
   for value in range(limit, limit + 6):
      outcomes[value] = 0

   for _ in range(trials):
      score = holdAt20(limit)
      outcomes[score] += 1


   for score in outcomes:
      print(score, outcomes[score]/trials)

#holdAt20()
holdAtXOutcomes(100000, 20)
#holdAt20Outcomes(100000)
