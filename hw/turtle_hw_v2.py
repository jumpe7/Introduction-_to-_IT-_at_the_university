import turtle as t

class Draw_figures:
    def __init__(self, figure):
        self.figure = figure

    def draw_circle(self):
        radius = 30
        current_position = t.pos()
        current_peading = t.heading()

        t.penup()
        t.sety(t.ycor() - radius)
        t.setheading(0)
        t.pendown()

        t.circle(radius)

        t.penup()
        t.goto(current_position)
        t.setheading(current_peading)
        t.pendown()

    def drawing(self):
        t.clear()
        match self.figure:
            case "треугольник":
                sides = 120

                for _ in range(3):
                    t.forward(200)
                    self.draw_circle()
                    t.left(sides)

            case "круг":

                    t.circle(200)

            case "квадрат":
                    sides = 90
                    
                    for _ in range(4):
                         t.forward(200)
                         self.draw_circle()
                         t.left(sides)


status = True
figure = ("треугольник", "круг", "квадрат")

while status:
    input_figure = input("Введите фигуру: ")
    if input_figure.lower() in figure:
        result = Draw_figures(input_figure)
        result.drawing()
        status = False
    else:
        print("not succes")


if __name__ == "__main__":
     t.Screen()
     t.color("black")
     t.speed(6)
     t.done()