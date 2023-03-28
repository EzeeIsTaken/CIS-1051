import turtle

bob = turtle.Turtle()

def drawSquare(bob, side):
   for i in range(4):   
      bob.forward(side)
      bob.right(90)


 


def drawVertical(bob):
   for i in range(4):
      drawSquare(bob, 100)
      bob.right(90)
      bob.forward(100)
      bob.left(90)


drawVertical(bob)
