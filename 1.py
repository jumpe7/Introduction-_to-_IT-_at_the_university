import turtle
import math
import tkinter as tk
from tkinter import messagebox


def draw_circle(radius):
    """Рисует окружность в текущей вершине многоугольника."""
    current_pos = turtle.pos()
    current_heading = turtle.heading()

    # Смещаемся вниз на радиус, чтобы центр окружности был в вершине
    turtle.penup()
    turtle.sety(turtle.ycor() - radius)
    turtle.setheading(0)
    turtle.pendown()

    turtle.circle(radius)

    # Возвращаемся в исходную точку и направление
    turtle.penup()
    turtle.goto(current_pos)
    turtle.setheading(current_heading)
    turtle.pendown()


def draw_polygon_with_circles(sides, circle_radius):
    """Рисует многоугольник с окружностями в вершинах."""
    # Настройки экрана
    screen = turtle.Screen()
    screen.title("Многоугольник с окружностями в вершинах")
    screen.setup(width=800, height=800)
    turtle.speed(5)
    turtle.clear()

    polygon_radius = 150
    side_length = 2 * polygon_radius * math.sin(math.pi / sides)
    exterior_angle = 360 / sides

    # Сдвигаем черепашку, чтобы фигура была по центру
    turtle.penup()
    turtle.goto(0, -polygon_radius)
    turtle.pendown()

    for _ in range(sides):
        draw_circle(circle_radius)
        turtle.forward(side_length)
        turtle.left(exterior_angle)

    turtle.hideturtle()
    screen.mainloop()


def start_drawing():
    """Считывает данные из полей ввода и запускает рисование."""
    try:
        sides = int(entry_sides.get())
        radius = float(entry_radius.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, вводите только числа.")
        return

    if sides < 3:
        messagebox.showerror("Ошибка", "Количество углов должно быть 3 или более.")
        return

    if radius <= 0:
        messagebox.showerror("Ошибка", "Радиус должен быть положительным.")
        return

    # Закрываем окно ввода и запускаем рисование
    root.destroy()
    draw_polygon_with_circles(sides, radius)


# --- Окно ввода (tkinter) ---
root = tk.Tk()
root.title("Параметры фигуры")
root.geometry("320x200")
root.resizable(False, False)

tk.Label(root, text="Количество углов многоугольника:").pack(pady=(15, 0))
entry_sides = tk.Entry(root, justify="center")
entry_sides.pack(pady=5)
entry_sides.insert(0, "5")

tk.Label(root, text="Радиус окружностей в вершинах:").pack(pady=(10, 0))
entry_radius = tk.Entry(root, justify="center")
entry_radius.pack(pady=5)
entry_radius.insert(0, "20")

tk.Button(root, text="Нарисовать", command=start_drawing, width=20).pack(pady=15)

root.mainloop()