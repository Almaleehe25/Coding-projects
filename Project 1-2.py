import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.color("red")
t.begin_fill()
for i in range(150):
  t.forward(10)
  t.right(360/100)
t.end_fill()
