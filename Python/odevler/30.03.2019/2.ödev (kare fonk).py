import turtle
import random

kalem=turtle.Turtle()
rasty = random.randrange(10,500)
for i in range(50):
    rastkare = random.randrange(10,50)
    for i in range(4):
        kalem.pd()
        kalem.fd(rastkare)
        kalem.rt(90)
        kalem.pu()
    kalem.goto(random.randrange(10,500),random.randrange(10,500))
    

