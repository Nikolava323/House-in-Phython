from turtle import *

#Square
width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#Door
color("black")
penup()
goto(80, 0)
pendown()
begin_fill()
left(90)
forward(80)

right(90)
forward(40)

right(90)
forward(80)
end_fill()

#Roof
color("yellow")
penup()
goto(200, 200)
pendown()
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()
left(120)

#windows
color("purple")
penup()
goto(20 , 180)
pendown()
begin_fill()
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)
end_fill()
right(90)


penup()  #second window
goto(120 , 180)
pendown()
begin_fill()
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)
right(90)
end_fill()

#Grass
speed(10)
color("green")
penup()
goto(-1000 ,0)
pendown()
begin_fill()
forward(2200)

right(90)
forward(1000)

right(90)
forward(2200)

right(90)
forward(1000)
end_fill()


exitonclick()