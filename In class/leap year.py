def isLeapYear(year):
   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0:
            return True
         else:
            return False
      else:
         return False
   else:
      return False

date = input("Please enter a date in MM/DD/YYYY format")

month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])

if month in [4,6,9,11]:
   if 1 <= day <= 30:
      print("Valid Date")
   else:
      print("Invalid Day")
         
elif month in [1,3,5,7,8,10,12]:
      if 1 <= day <= 31:
         print("Valid Date")
      else:
         print("Invalid Day")
         

elif month == 2:
   if 1 <= day <= 28:
      print("Valid Date")
   elif day == 29:
      if isLeapYear(year):
         print("Valid Date")
      else:
         print("Invalid Day, not a leap year")
   
      
   else:
      print("Invalid Month")
