import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.pensize(2)
bob.shape("turtle")

for i in range(3):
   bob.fd(100)
   bob.left(120)

bob.fd(50)
bob.right(60)

for i in range(3):
   bob.left(120)
   bob.fd(50)

bob.hideturtle()
