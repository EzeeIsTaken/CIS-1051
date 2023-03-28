import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.pensize(2)
bob.shape("turtle")

x = int(input("How many sides to this shape?"))

for i in range(x):
   bob.fd(45)
   bob.left(360/x)
