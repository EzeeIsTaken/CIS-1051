import turtle
bob = turtle.Turtle()
bob.speed(0)

def drawSquare(bob, size):
   for i in range(4):
      bob.forward(size)
      bob.right(90)

def drawRow(bob, length, size):
   for i in range(length):
      drawSquare(bob, size)
      bob.forward(size)

def drawGrid(bob, grid, size):
   for i in range(grid):
      drawRow(bob, grid, size)
      bob.penup()
      bob.goto(0,0)
      bob.right(90)
      bob.forward((size*i)+size)
      bob.left(90)
      bob.pendown()

def drawSquareStairs(bob, height, size):
   for i in range(height):
      drawRow(bob, i+1, size)
      bob.penup()
      bob.goto(0,0)
      bob.right(90)
      bob.forward((size*i)+size)
      bob.left(90)
      bob.pendown()

def drawNgon(bob, numSides, numLength):
   for i in range(numSides):
      bob.forward(numLength)
      bob.left(360/numSides)
      
color = ['green', 'red', 'blue', 'pink', 'yellow', 'purple']
def drawNgonSpiral(bob, numSides, numLength, numShapes):
   for i in range(numShapes):
      bob.left(360/numShapes)
      for i in range(numSides):
         bob.color(color[i])
         bob.forward(numLength)
         bob.left(360/numSides)


