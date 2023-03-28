data = open("hamlet.txt", 'r', encoding = "utf8")
#text = data.read()

#print(text.lower().count("hamlet"))


lines = data.readlines()


print(lines[:50])


#for line in data:
#   print(line)
