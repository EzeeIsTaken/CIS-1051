singleVowels = {"a": "ah",
               "e": "eh",
               "i": "ee",
               "o": "oh",
               "u": "oo"}

doubleVowels = {"ai": "eye",
                "ae": "eye",
                "ao": "ow",
                "au": "ow",
                "ei": "ay",
                "eu": "eh-oo",
                "iu": "ew",
                "oi": "oyo", }

cons =  "wphkmln"


def validate(word):
    for letter in word:
        if letter not in cons or singleVowels: #finish this: is not a valid letter in hawaiin words       
        
    return True

def pronounce(word):
    output = ""
    i = 0 # i is the index
    while i < len(word):
        if word[i:i+2] in doubleVowels:
            print(word[i:i+2])
            i+=2
        elif word[i] in singleVowel:
            print(word[i])
            i+=1
        elif word[i] in cons:
            print(word[i])
            output+=word[i]
            i+=1
        elif word[i] == "'":
            print(word[i])
            i+=1
    print(output, end = " ")


def main():
    done = False
    while not done:

        gaveValidWord = False
        while not gaveValidWord:
            word = input("give word")
            gaveValidWord = validate(word)

        response = input("go again?")
        if response == "no way!":
            done = True

#pronounce("keiki")
main()
