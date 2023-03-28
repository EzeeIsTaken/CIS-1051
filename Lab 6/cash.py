def main_function():
   
   change_owe = input('What is the amount of change owed?')
   coins = 0

   try:
      change_owe = float(change_owe)
      pass
   except:
      main_function()

   if change_owe < .01:
      main_function()
   

   rounded_owe = round(float(change_owe)*100)


   def whichCoins(remaining):
      if(remaining - 25 >= 0):
         return 25
      elif(remaining - 10 >= 0):
         return 10
      elif(remaining - 5 >= 0):
         return 5
      else:
         return 1

   while(rounded_owe > 0):
      rounded_owe -= whichCoins(rounded_owe)
      coins += 1

   print('Change owed:', change_owe)
   print(coins)


main_function()
