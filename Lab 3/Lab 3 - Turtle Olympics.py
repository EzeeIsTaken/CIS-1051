import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.pensize(3)
bob.shape("turtle")

pi = 3.141519
radius = 50
circf = 2*pi*radius

def circle():
   for _ in range(40):
      bob.fd(circf/40)
      bob.left(360/40)

bob.color("blue")
circle()
r = 0
f = 0

c = ["yellow", "black", "green", "red"]

bob.penup()
bob.right(r + 45)
bob.fd(45 - f)
bob.pendown()
bob.color(c[0])
circle()
   
 
bob.left(60)
bob.penup()
bob.fd(115)
bob.pendown()
bob.color(c[1])
circle()

r += 20
f += 10

bob.penup()
bob.right(r + 45)
bob.fd(45 - f)
bob.pendown()
bob.color(c[2])
circle()
   
 
bob.left(60)
bob.penup()
bob.fd(115)
bob.pendown()
bob.color(c[3])
circle()

bob.hideturtle()
