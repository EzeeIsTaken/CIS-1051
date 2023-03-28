#Female
weight = int(input("What is your weight?"))
height = int(input("What is your height?"))
age = int(input("What is your age?"))

bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
chocolate = bmr/214
print("bmr for female", bmr)
print("As a female you would need chocolate", chocolate, "choclate bars to maintain your weight")

#Male


bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
chocolate = bmr/214

print("As a male you would need chocolate", chocolate, "choclate bars to maintain your weight")
