from turtle import *

t = Turtle()
w = t.getscreen()

def drawSpiral(t: Turtle, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen-5)

drawSpiral(t, 100)
w.exitonclick()