def numVowels(word):
   count = 0
   vowels = "aeiou" #["a", "e", "i", "o", "u"]
   word = word.lower()
   for letter in word:
      if letter in vowels:
         count += 1
   return count
#

def numEvenDigits(number):
   count = 0
   origin = number
   even = "02468" #[0, 2, 4, 6, 8]
   for d in str(number):
         if d in even:
            count += 1
   return count
#

def isArmstrong(num):
   total = 0
   origin = num
   
   while num > 0:
      lastDigit = num % 10
      
      total = total + lastDigit**3
              
      num = num // 10
      
   if total == origin:
      return True
   else:
      return False
#

def riddler():
   for number in range(1001, 10000, 2):
      thou = number // 1000
      hund = number // 100 % 10
      tens = number // 10 % 10
      ones = number % 10

      if thou != hund and thou != tens and thou != ones and hund != tens and hund != ones and tens != ones:
         if 3 * tens == thou:
            if thou + hund + tens + ones == 27:
               print(number)

riddler()
