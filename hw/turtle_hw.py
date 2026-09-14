import turtle

def draw_circle(radius):
    """
    Draws a circle with a specified radius at the current turtle position,
    then returns the turtle to its original position and heading.
    Accepts a radius parameter to allow for different circle sizes.
    """
    current_position = turtle.pos()
    current_heading = turtle.heading()

    turtle.penup()
    turtle.sety(turtle.ycor() - radius)
    turtle.setheading(0)
    turtle.pendown()

    turtle.circle(radius)

    turtle.penup()
    turtle.goto(current_position)
    turtle.setheading(current_heading)
    turtle.pendown()

N_angles = int(input("введите количество углов многоугольника: "))
Radius = int(input("Введите радиус: "))
turtle.speed(3)
turtle.color("black")

Sides = 360/N_angles
lenght = 80

for _ in range(N_angles):
    turtle.forward(150)
    draw_circle(Radius)
    turtle.left(Sides)

turtle.Screen()
turtle.mainloop()