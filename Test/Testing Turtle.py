import turtle
bob = turtle.Turtle()


def drawSquare(bob, side):
    for i in range(4):
        bob.forward(side)
        bob.right(90)


def fourSquare(bob):
   side = 50
   for i in range(4):
      drawSquare(bob, side)
   
      bob.forward(side/2)
      bob.right(90)
      bob.penup()
      bob.forward(side/2)
      bob.left(90)
      bob.pendown()


def moveNext():
   bob.forward(side/2)
   bob.right(90)
   bob.forward(side/2)
   bob.left(90)

fourSquare(bob)
