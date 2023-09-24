import turtle
import random
import time
from pygame import mixer




bg = turtle.Screen()
bg.bgcolor("black")




turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)


turtle.penup()
turtle.goto(-145,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)


turtle.penup()
turtle.goto(-120,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")


turtle.penup()
turtle.goto(-65,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("black")


turtle.penup()
turtle.goto(-55,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-25,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(5,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(35,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(65,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("lightblue")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-5,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("black")



turtle.penup()
turtle.goto(-130, 50)
turtle.color("skyblue")
turtle.pendown()


turtle.write(arg=f"Happy Birthday!", align="left", font=("style", 24, "normal"))

time.sleep(5)