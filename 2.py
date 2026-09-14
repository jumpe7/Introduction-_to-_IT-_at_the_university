import turtle

def draw_circle()

status = True
while status:
    user_figure = str(input("Введи фигуру: "))
    if user_figure == 'треугольник' or user_figure == 'квадрат' or user_figure == 'круг':
        print("input correct")
        status = False
    else:
        print('input not correct')