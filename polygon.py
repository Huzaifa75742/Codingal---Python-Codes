import turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(300,400)
polygon = turtle.Turtle()

num_sides = 8
length = 70
angle = 360 / num_sides
for _ in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()