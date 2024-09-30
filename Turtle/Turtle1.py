import turtle

t=turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.color("white")
def fun(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

size=0
for i in range(61):
    
    if i%10==0:
        size+=10
        fun(size)