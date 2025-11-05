from turtle import *

def tree(branchLen, t: Turtle):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)


t = Turtle()
w = t.getscreen()


tree(100, t)
w.exitonclick()