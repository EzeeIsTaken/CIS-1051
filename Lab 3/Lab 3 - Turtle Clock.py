import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.pensize(2)
bob.shape("turtle")

for i in range(12):
   bob.penup()
   bob.fd(100)
   bob.pendown()
   bob.fd(50)
   bob.penup()
   bob.fd(25)
   bob.stamp()
   bob.backward(175)
   bob.right(360/12)
