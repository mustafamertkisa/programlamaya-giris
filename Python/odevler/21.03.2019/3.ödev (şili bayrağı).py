import turtle
a=turtle.Turtle()
a.speed(0)
a.pu()
a.sety(-75)
a.pencolor("red")
a.begin_fill()
a.color("red")
for i in range(2):
    a.fd(500)
    a.lt(90)
    a.fd(150)
    a.lt(90)
    a.pd()
a.end_fill()
a.pu()
a.sety(75)
a.pencolor("white")
a.begin_fill()
a.color("white")
for i in range(2):
    a.fd(500)
    a.lt(90)
    a.fd(150)
    a.lt(90)
    a.pd()
a.end_fill()
a.pu()
a.sety(75)
a.pencolor("#1b06a9")
a.begin_fill()
a.color("#1b06a9")
for i in range(2):
    a.fd(150)
    a.lt(90)
    a.fd(150)
    a.lt(90)
    a.pd()
a.end_fill()
a.goto(105,110)
a.begin_fill()
a.color("white")
a.rt(34)
for i in range(6):   
    a.lt(144)
    a.fd(90)
    a.pd()
a.end_fill()
a.pu()
a.home()
