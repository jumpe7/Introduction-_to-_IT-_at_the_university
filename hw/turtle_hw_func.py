import turtle as t
def draw_circles():
        """
        Draws a circle with a radius of 30 at the current turtle position, 
        then returns the turtle to its original position and heading.
        """
        radius = 30
        current_position = t.pos()
        current_heading = t.heading()

        t.penup()
        t.sety(t.ycor() - radius)
        t.setheading(0)
        t.pendown()

        t.circle(radius)

        t.penup()
        t.goto(current_position)
        t.setheading(current_heading)
        t.pendown()

def draw_triangle():
        """
        Draws a triangle with circles at each vertex.
        """
        sides = 120

        for _ in range(3):
            t.forward(200)
            draw_circles()
            t.left(sides)

def draw_square():
        """
        Draws a square with circles at each vertex.
        """
        sides = 90
        
        for _ in range(4):
                t.forward(200)
                draw_circles()
                t.left(sides)

def draw_circle():
        """
        Draws a circle with a radius of 200.
        """
        t.circle(200)

def drawing(figure):
    """ Draws the specified figure (triangle, circle, or square) using turtle graphics."""
    t.clear()
    match figure:
        case "треугольник":
            draw_triangle()

        case "круг":
            draw_circle()

        case "квадрат":
                draw_square()

status = True
figure = ("треугольник", "круг", "квадрат")

while status:
    input_figure = input("Введите фигуру: ")
    if input_figure.lower() in figure:
        drawing(input_figure)
        t.Screen()
        t.color("black")
        t.speed(6)
        t.done()
        status = False
    else:
        print("not succes")