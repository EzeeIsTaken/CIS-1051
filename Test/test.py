#total = 0
#for i in range(2):
#   total = total + i
#
#print(total)
"""
pi4 = 0
sign = 1

for dom in range(1, 10, 2):
   print(pi4, "+", sign*1/dom, "=", pi4 + sign*1/dom)
   pi4 = pi4 + sign*1/dom
   sign *= -1
print("done. sum is", pi4)
print("pi ~=", 4*pi4)
"""

import turtle

bob = turtle.Turtle()
bob.shapesize(3,3)
bob.pensize(5)
bob.color("red")
bob.shape("turtle")
bob.speed(10)

for i in range(50):
   bob.fd(100)
   bob.right(90 + 5)
