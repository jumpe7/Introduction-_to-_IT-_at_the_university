import turtle
def draw_circle(radius):
        current_position = turtle.pos()
        current_heading = turtle.heading()


        turtle.pen()
        turtle.penup()
        turtle.sety(turtle.ycor() - radius)
        turtle.setheading(0)
        turtle.pendown()
        
        turtle.circle(radius)

        


N_angels = int(input("Введите количество углов многоугольника: "))
Radius = int(input("Введите радиус углов: "))


screen = turtle.Screen()
turtle.speed(5)

exterior_angle = 360/N_angels
for _ in range(N_angels):

        turtle.forward(150)
        draw_circle(Radius)
        turtle.left(exterior_angle)
screen.mainloop()