import turtle
import math
import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
#                РИСОВАНИЕ ОСНОВНОЙ ФИГУРЫ
# ============================================================

def draw_shape(t, sides, side_length, corner_mode, corner_size, is_regular):
    """
    Рисует одну фигуру.
    
    t            — черепашка
    sides        — количество углов
    side_length  — длина стороны
    corner_mode  — 'circle' | 'polygon' | 'none'
    corner_size  — радиус окружности или длина стороны угловой фигуры
    is_regular   — True = правильный многоугольник (равные стороны),
                   False = просто N углов (замыкаем произвольно)
    """
    exterior_angle = 360 / sides

    for _ in range(sides):
        # 1. Рисуем фигуру в вершине
        if corner_mode == 'circle':
            draw_circle(t, corner_size)
        elif corner_mode == 'polygon':
            draw_small_polygon(t, sides, corner_size)

        # 2. Идём по стороне и поворачиваем
        t.forward(side_length)
        t.left(exterior_angle)


def draw_circle(t, radius):
    """Рисует окружность в текущей вершине."""
    pos = t.pos()
    heading = t.heading()

    t.penup()
    t.sety(t.ycor() - radius)
    t.setheading(0)
    t.pendown()

    t.circle(radius)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()


def draw_small_polygon(t, sides, side_length):
    """Рисует маленький многоугольник с тем же числом углов в вершине."""
    pos = t.pos()
    heading = t.heading()

    # Чтобы центр фигуры оказался в вершине, сдвигаемся назад
    # на радиус описанной окружности маленького многоугольника
    r = side_length / (2 * math.sin(math.pi / sides)) if sides > 2 else side_length / 2

    t.penup()
    t.sety(t.ycor() - r)
    t.setheading(0)
    t.pendown()

    exterior_angle = 360 / sides
    for _ in range(sides):
        t.forward(side_length)
        t.left(exterior_angle)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()


# ============================================================
#                ЗАПУСК ЧЕРЕПАШКИ
# ============================================================

def run_turtle(params):
    """Открывает окно черепашки и рисует фигуру по параметрам."""
    screen = turtle.Screen()
    screen.clear()
    screen.setup(width=params['window_w'], height=params['window_h'])
    screen.title("Рисование фигур")

    t = turtle.Turtle()
    t.speed(0)          # максимальная скорость
    t.hideturtle()

    # Центрируем фигуру
    t.penup()
    t.goto(0, -params['polygon_radius'])
    t.pendown()
    t.showturtle()

    draw_shape(
        t,
        sides=params['sides'],
        side_length=params['side_length'],
        corner_mode=params['corner_mode'],
        corner_size=params['corner_size'],
        is_regular=params['is_regular']
    )

    t.hideturtle()

    # Кнопка «Ещё раз» на экране черепашки
    def ask_again():
        screen.bye()          # закрыть окно черепашки
        open_input_window()   # открыть окно ввода заново

    screen.onkey(ask_again, "space")
    screen.listen()

    # Подсказка в консоли
    print("Рисование завершено. Нажмите ПРОБЕЛ в окне черепашки, чтобы выбрать новую фигуру.")
    print("Или просто закройте окно для выхода.")

    screen.mainloop()


# ============================================================
#                ОКНО ВВОДА ПАРАМЕТРОВ
# ============================================================

def open_input_window():
    root = tk.Tk()
    root.title("Параметры фигуры")
    root.geometry("420x560")
    root.resizable(False, False)

    # ---------- Выбор фигуры ----------
    tk.Label(root, text="Фигура:", font=("Arial", 11, "bold")).pack(pady=(15, 0))

    shape_var = tk.StringVar(value="circle")
    shapes_frame = tk.Frame(root)
    shapes_frame.pack(pady=5)

    tk.Radiobutton(shapes_frame, text="Круг", variable=shape_var,
                   value="circle").grid(row=0, column=0, padx=10)
    tk.Radiobutton(shapes_frame, text="Квадрат", variable=shape_var,
                   value="square").grid(row=0, column=1, padx=10)
    tk.Radiobutton(shapes_frame, text="Треугольник", variable=shape_var,
                   value="triangle").grid(row=0, column=2, padx=10)

    # ---------- Количество углов ----------
    tk.Label(root, text="Количество углов многоугольника:").pack(pady=(15, 0))
    entry_sides = tk.Entry(root, justify="center")
    entry_sides.pack(pady=5)
    entry_sides.insert(0, "5")

    # ---------- Размер фигуры ----------
    tk.Label(root, text="Размер фигуры (длина стороны):").pack(pady=(10, 0))
    entry_size = tk.Entry(root, justify="center")
    entry_size.pack(pady=5)
    entry_size.insert(0, "100")

    # ---------- Что рисовать в углах ----------
    tk.Label(root, text="Что рисовать в углах:", font=("Arial", 11, "bold")).pack(pady=(15, 0))

    corner_var = tk.StringVar(value="circle")
    corner_frame = tk.Frame(root)
    corner_frame.pack(pady=5)

    tk.Radiobutton(corner_frame, text="Окружность", variable=corner_var,
                   value="circle").grid(row=0, column=0, padx=10)
    tk.Radiobutton(corner_frame, text="Такую же фигуру", variable=corner_var,
                   value="polygon").grid(row=0, column=1, padx=10)
    tk.Radiobutton(corner_frame, text="Ничего", variable=corner_var,
                   value="none").grid(row=0, column=2, padx=10)

    # ---------- Размер фигур в углах ----------
    tk.Label(root, text="Размер фигур в углах (радиус/сторона):").pack(pady=(10, 0))
    entry_corner_size = tk.Entry(root, justify="center")
    entry_corner_size.pack(pady=5)
    entry_corner_size.insert(0, "20")

    # ---------- Размер окна черепашки ----------
    tk.Label(root, text="Размер окна черепашки (Ш x В):").pack(pady=(15, 0))
    window_frame = tk.Frame(root)
    window_frame.pack(pady=5)

    entry_w = tk.Entry(window_frame, width=6, justify="center")
    entry_w.grid(row=0, column=0, padx=5)
    entry_w.insert(0, "800")

    tk.Label(window_frame, text="x").grid(row=0, column=1)

    entry_h = tk.Entry(window_frame, width=6, justify="center")
    entry_h.grid(row=0, column=2, padx=5)
    entry_h.insert(0, "800")

    # ---------- Радиус описанной окружности ----------
    tk.Label(root, text="Радиус описанной окружности (масштаб):").pack(pady=(10, 0))
    entry_polygon_radius = tk.Entry(root, justify="center")
    entry_polygon_radius.pack(pady=5)
    entry_polygon_radius.insert(0, "200")

    # ---------- Кнопка ----------
    def on_draw():
        try:
            sides = int(entry_sides.get())
            side_length = float(entry_size.get())
            corner_size = float(entry_corner_size.get())
            win_w = int(entry_w.get())
            win_h = int(entry_h.get())
            polygon_radius = float(entry_polygon_radius.get())
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, вводите только числа.")
            return

        if sides < 3:
            messagebox.showerror("Ошибка", "Количество углов должно быть 3 или более.")
            return
        if side_length <= 0 or corner_size < 0:
            messagebox.showerror("Ошибка", "Размеры должны быть положительными.")
            return
        if win_w < 200 or win_h < 200:
            messagebox.showerror("Ошибка", "Размер окна должен быть не меньше 200x200.")
            return

        # Определяем, какая фигура выбрана
        shape = shape_var.get()
        if shape == "square":
            sides = 4
        elif shape == "triangle":
            sides = 3
        # если "circle" — sides берётся из поля «Количество углов»

        corner_mode = corner_var.get()

        params = {
            'sides': sides,
            'side_length': side_length,
            'corner_mode': corner_mode,
            'corner_size': corner_size,
            'is_regular': True,
            'window_w': win_w,
            'window_h': win_h,
            'polygon_radius': polygon_radius,
        }

        root.destroy()
        run_turtle(params)

    tk.Button(root, text="Нарисовать", command=on_draw,
              width=25, height=2, bg="#4CAF50", fg="white",
              font=("Arial", 11, "bold")).pack(pady=20)

    root.mainloop()


# ============================================================
#                        ЗАПУСК
# ============================================================

if __name__ == "__main__":
    open_input_window()