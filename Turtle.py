import turtle 
from turtle import *
s = turtle.Screen()
s.bgcolor("#888")
x = turtle.Turtle()
e = turtle.Turtle()
s = turtle.Turtle()
i = turtle.Turtle()


len = 550
h = 100
i.pensize(2)
i.speed(10)
s.pensize(2)
s.speed(10)
i.up()
s.up()
i.lt(90)
s.lt(90)
i.fd(330)
s.fd(330)
i.lt(90)
s.rt(90)
i.fd(640)
s.fd(90)
i.rt(90)
i.down()
s.down()

i.fillcolor("red")
s.fillcolor("#009736")
i.color("red")
s.color("#009736")
i.begin_fill()
s.begin_fill()
i.rt(90)
i.fd(len)
s.fd(len)
i.rt(90)
s.rt(90)
i.fd(h)
s.fd(h)
i.rt(90)
s.rt(90)
i.fd(len)
s.fd(len)
i.end_fill()
s.end_fill()

i.fillcolor("white")
s.fillcolor("white")
i.begin_fill()
s.begin_fill()
i.color("white")
s.color("white")
i.lt(90)
s.lt(90)
i.fd(h)
s.fd(h)
i.lt(90)
s.lt(90)
i.fd(len)
s.fd(len)
i.lt(90)
s.lt(90)
i.fd(h)
s.fd(h)
i.end_fill()
s.end_fill()

i.lt(180)
s.lt(180)
i.fd(h)
s.fd(h)

i.fillcolor("black")
s.fillcolor("black")
i.color("black")
s.color("black")
i.begin_fill()
s.begin_fill()
i.fd(h)
s.fd(h)
i.rt(90)
s.rt(90)
i.fd(len)
s.fd(len)
i.rt(90)
s.rt(90)
i.fd(h)
s.fd(h)
i.end_fill()
s.end_fill()

s.up()
s.fd(60)
s.rt(90)
s.fd(90)
s.down()

i.up()
i.fd(10)
i.color("green")
i.shapesize(0.01)
i.rt(90)
i.fd(180)
i.write("الله أكبر", font=("Aria", 50, "bold"))

s.fillcolor("#ee2a35")
s.color("#ee2a35")
s.begin_fill()
angle = 144
slen = 80
fd = 150
s.fd(slen)
for i in range(4):
    s.rt(angle)
    s.fd(slen)
s.end_fill()

s.up()
s.rt(144)
s.fd(fd)
s.down()
s.fillcolor("#ee2a35")
s.color("#ee2a35")
s.begin_fill()
s.fd(slen)
for i in range(4):
    s.rt(angle)
    s.fd(slen)
s.end_fill()

s.up()
s.rt(144)
s.fd(fd)
s.down()
s.fillcolor("#ee2a35")
s.color("#ee2a35")
s.begin_fill()
s.fd(slen)
for i in range(4):
    s.rt(angle)
    s.fd(slen)
s.shapesize(0.01)
s.end_fill()

x.pensize(2)
x.speed(10)
e.pensize(2)
e.speed(10)
x.up()
e.up()
x.rt(90)
e.rt(90)
x.fd(20)
e.fd(20)
x.lt(90)
e.rt(90)
x.fd(90)
e.fd(90 + 550)
e.rt(180)
x.down()
e.down()

x.fillcolor("black")
e.fillcolor("red")
e.color("red")
x.begin_fill()
e.begin_fill()
x.fd(len)
e.fd(len)
x.rt(90)
e.rt(90)
x.fd(h)
e.fd(h)
x.rt(90)
e.rt(90)
x.fd(len)
e.fd(len)
x.end_fill()
e.end_fill()

x.fillcolor("white")
e.fillcolor("white")
x.begin_fill()
e.begin_fill()
x.color("white")
e.color("white")
x.lt(90)
e.lt(90)
x.fd(h)
e.fd(h)
x.lt(90)
e.lt(90)
x.fd(len)
e.fd(len)
x.lt(90)
e.lt(90)
x.fd(h)
e.fd(h)
x.end_fill()
e.end_fill()

x.lt(180)
e.lt(180)
x.fd(h)
e.fd(h)

x.fillcolor("#009736")
e.fillcolor("#000")
x.color("#009736")
e.color("#000")
x.begin_fill()
e.begin_fill()
x.fd(h)
e.fd(h)
x.rt(90)
e.rt(90)
x.fd(len)
e.fd(len)
x.rt(90)
e.rt(90)
x.fd(h)
e.fd(h)
e.shapesize(0.01)
x.end_fill()
e.end_fill()

x.up()
x.down()

x.fillcolor("#ee2a35")
x.color("#ee2a35")
x.begin_fill()
x.fd(200)
x.rt(360/3)
x.fd(300)
x.rt(360/3)
x.fd(300)
x.rt(360/3)
x.fd(300)
x.shapesize(0.01)
x.end_fill()

done()
