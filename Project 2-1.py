import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.color("blue")
for j in range(6):
  #t.begin_fill()
  for i in range(30):
    t.forward(10)
    t.right(15)
  #t.end_fill()
  t.forward(100)
  t.left(30)
