consonants = ('p','k','h','l','m','n')

def check(valid, word):
    for x in word:
        x = x.lower()
        if valid.count(x) == 0:
            print(x, "is not a valid hawaiian word")
            return False
    return True
def convert(word):
   convert = ""
   x = 0
   while x < len(word)-1:
        word = word.lower()    
        if word[x] == "a":
            after_x = word[x+1]
            if after_x == "i" or after_x == "e":
                convert = convert + "eye-"
                x = x+1
            elif after_x == 'o' or after_x == "u":
                convert = convert + "ow-"
                x=x+1
            else:
                convert = convert + "ah-" 
        elif word[x] == "e":
            after_x = word[x+1]
            if after_x == "i":
                convert = convert + "ay-"
                x = x+1
            elif after_x == 'u':
                convert = convert + "eh-oo-"
                x= x+1
            elif after_x == 'w': #
                convert = convert + "v"
                x=x+1
            else:
                convert = convert + "eh-"
        elif word[x] == "i":
            after_x = word[x+1]
            if after_x == "u":
                convert = convert + "ew-"
                x = x+1
            else:
                convert = convert + "ee-"        
        elif word[x] == "o":
            after_x = word[x+1]
            if after_x == "i":
                convert = convert + "oy-"
                x = x+1
            elif after_x == "u":
                convert = convert + "ow-"
                x = x+1
            elif after_x == 'w': #
                convert = convert + "v"
                x = x+1
            else:
                convert = convert + "oh-"   
        elif word[x] == "u":
            after_x = word[x+1]
            if after_x == "i":
                convert = convert + "ooey-"
                x = x+1
            else:
                convert = convert + "oo-"
        elif word[x] == consonants:
            convert = convert + consonants        
        elif word[x] == " " and convert[len(convert)-1] == "-":
            convert = convert[0:len(convert)-1] + " "
        elif word[x] == "\'" and convert[len(convert)-1] == "-":
            convert = convert[0:len(convert)-1] + "'"
        else:
            convert = convert + word[x]
        x = x +1 
        if x < len(word):
            m = word[len(word)-1]
            m = m.lower()
            if m == "a" or m == "e" or m == "o":
                convert = convert + m + "h"
            elif m == "i":
                convert = convert + "ee"
            elif m == "u":
                convert = convert + "oo"
            else:
                convert = convert + m
        if convert[len(convert)-1] == '-':
            convert = convert[0:len(convert)-1]
        convert = convert.upper()
        return convert
def main():
    valid = ['p','k','h','l','m','n','w','a','e','i','o','u', ' ', '\'']
    while True:
        word = input("Enter a Hawaiian Word to Pronounce")
        word = word.strip()
        if(check(valid,word)):
            converted_word = convert(word)
            converted_word = converted_word.upper()
            print(word + " is pronounced" , converted_word)          
        repeat = input("Would you like to enter another word Y/YES/N/NO")
        repeat = repeat.upper()
        if repeat == 'N' or repeat == 'NO':
            break
        else:
            main()        
main()
