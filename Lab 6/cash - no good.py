owe = 0
coins = 0

def askChange(owe):
   owe = float(input("How much change is owed"))

def isFloat(owe):
   decAmount = owe.count["."]
   if decAmount > 1:
      askChange(owe)
   else:
      decWhere = owe.index(".")
      owe = owe[decWhere:]
#Use valueerror
   
askChange(owe)

while owe <= 0:
   askChange(owe)
   
if owe > 0:
   isFloat(owe)      

owe *= 100


while owe >= 25:
   owe -= 25
   coins += 1
   if owe <= 10:
      owe -= 10
      coins += 1
      if owe <= 5:
         owe -= 5
         coins += 1
         if owe < 5:
            owe -= 1
            coins += 1

print(coins)
