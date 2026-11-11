import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.color("blue")
t.begin_fill()
for i in range(30):
  t.forward(20)
  t.right(15)
t.end_fill()
t.penup()
t.forward(85)
t.right(90)
t.forward(60)
t.pendown()
t.color("black")
t.forward(20)
t.left(90)
t.forward(150)
t.hideturtle()
