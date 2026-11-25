
import turtle
t = turtle.Turtle()

#Change speed and color of the turtle
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

#R (red), G (green), B (blue)
t.color(250, 102, 176)

for j in range(12):
  #t.begin_fill()

  #Draw a circle
  '''
  for i in range(30):
    t.forward(10)
    t.right(15)
  '''

  t.begin_fill()
  #Draw a triangle
  t.right(120)
  t.forward(20)

  t.right(120)
  t.forward(20)

  t.right(120)
  t.forward(20)
  t.end_fill()

  #Going between circles
  t.penup()
  t.forward(50)
  t.left(30)
  t.pendown()

  
  #making smaller triagles  
t.setheading(0)
t.forward(40)
for j in range(10):
	t.left(35)
	t.forward(60)
	for a in range(4):
  	t.forward(30)
  	t.right(90)
