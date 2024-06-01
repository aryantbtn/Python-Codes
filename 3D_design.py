import turtle

turtle.bgcolor("black")

square = turtle.Turtle()
square.speed(18)
square.pencolor('red')
for i in range(560):
    square.forward(i)
    square.left(91)