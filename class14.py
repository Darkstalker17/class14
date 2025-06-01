import turtle
'''Polygon
Outline:
Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?'''
'''
turtle.Screen()
turtle.bgcolor("white")
polygon = turtle.Turtle()
sides = 9
length = 100
angle = 360/sides
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
'''


'''Star
Outline:
Write a program to draw a star using a turtle?
star = turtle.Turtle()
angle = 144
l = 200
star.right(75)
star.forward(l)
star.right(angle)
star.forward(l)
star.right(angle)
star.forward(l)
star.right(angle)
star.forward(l)
star.right(angle)
star.forward(l)
star.right(angle)
star.forward(l)'''



'''Spiral pattern
Outline:
Write a program to draw a square inside a square?'''
'''
spiral = turtle.Turtle()
size = 0
while True:
    for i in range(5):
        spiral.forward(size+1)
        spiral.left(90)
        size -= 5
    size += 1
'''
import random
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
def draw():
    for i in range(150):
        spiral.color(random.random(),random.random(),random.random())
        spiral.forward(2*i)
        spiral.left(121)
    spiral.penup()
    spiral.goto(0,0)
    spiral.pendown()
for j in range(6):
    spiral.penup()
    spiral.goto(random.randint(-200,200),random.randint(-200,200))
    spiral.pendown()
    draw()

turtle.done()