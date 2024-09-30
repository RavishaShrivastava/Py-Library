import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
color=["yellow","red","green","blue","violet","orange"]
t=turtle.Pen()
for i in range(360):
    t.pencolor(color[i%6])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)
