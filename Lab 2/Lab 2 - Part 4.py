seconds = int(input("Enter a number of seconds and I'll tell you how many hours that is "))
hours = seconds//3600
remainder = seconds%3600
minutes = remainder//60
seconds2 = seconds%60

print(seconds, "seconds is", hours, "hours", minutes, "minutes", seconds2, "seconds")
