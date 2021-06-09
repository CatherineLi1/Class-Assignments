# Catherine Li
# 260914784


from turtle import *
import random
import math


shape_size = int(input("Please give the size of your shape (1-5): "))
number_sides = int(input("Please give the number of sides of your other shape: "))

speed("fastest")

#move to location for rainbow
up()
forward(300)
down()

#draw a rainbow:
r = 300
while r > 150:
    #change color for every iteration
    if r == 300:
        color("red")
    elif r == 275:
        color("orange")
    elif r == 250:
        color("gold")
    elif r == 225:
        color("chartreuse3")
    elif r == 200:
        color("deep sky blue")
    elif r == 175:
        color("white")

    #draw with color
    begin_fill()
    left(90)
    circle(r,180)

    left(90)
    up()
    forward(2*r-25)
    down()
    end_fill()
    r -= 25


#move to location for rectangle
up()
color("sienna")
goto(-50,0)
down()

#draw a rectangle
for i in range(2):
    begin_fill()
    forward(100)
    left(90)
    forward(75)
    left(90)
    end_fill()

#move to location for triangle
up()
goto(-80,75)
down()

#draw triangle
begin_fill()
color("slate gray")
forward(160)
left(150)
forward(80/math.sqrt(3)*2)
left(60)
forward(80/math.sqrt(3)*2)
end_fill()

#move to location for smiley face
up()
goto(-200,-25)
down()

#draw a smiley face
begin_fill()
color("LightPink")
circle(75)
end_fill()

#draw first eye
goto(-195,-65)
color("salmon")
begin_fill()
circle(7)
end_fill()

#move to location for second eye
up()
goto(-140,-65)
down()

#draw second eye
begin_fill()
circle(7)
end_fill()

#move to location for mouth
up()
goto(-120,-95)
down()
left(60)

#draw mouth
begin_fill()
circle(-45,180)
end_fill()

#move to location for signature
up()
goto(250,-100)
down()
left(85)

#signature
begin_fill()
color("steel blue")
circle(25,200)
left(90)
forward(5)
left(90)
circle(-20,200)
left(90)
forward(5)
end_fill()

#move to location for input-sized shape
up()
goto(-75,-175)
down()

#input-sized shape
color("royalblue")
begin_fill()
for i in range (5):
    forward(shape_size*20)
    right(360/5)
end_fill()

#move to location for random-sized shape
up()
goto(0,-150)
down()

#draw random-sized shape with input number of sides
color("wheat")
begin_fill()
length_side = random.randint(50,100)
for i in range (number_sides):
    forward(length_side)
    right(360/number_sides)
end_fill()
color("tan")

#outline shape in different color
for i in range (number_sides):
    forward(length_side)
    right(360/number_sides)