import turtle
import math


def draw_pythagoras_tree(t, length, level):
    """
    :param t: The turtle object used for drawing.
    :param length: The length of the base of the pythagoras tree.
    :param level: The level of recursion to draw the pythagoras tree.

    :return: None

    This method uses recursion to draw a pythagoras tree using the turtle graphics library.
    It takes in the turtle object 't', the length of the base 'length', and the level of recursion 'level'.
    The turtle starts by moving forward by 'length', then branches out in a V shape.
    For each branch, the method recursively calls itself with a shorter length and decreased level.
    The recursion ends when the level reaches 0, where the turtle simply moves backward the same length.
    """
    if level == 0:
        t.forward(length)
        t.backward(length)
        return
    # Рисуємо основний прямокутник
    t.forward(length)
    t.left(45)
    # Рекурсивно малюємо ліве гілля
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.right(90)
    # Рекурсивно малюємо праве гілля
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
    t.left(45)
    t.backward(length)


def main():
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed("fastest")

    # Встановлення початкової позиції
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    # Введення рівня рекурсії
    level = int(screen.numinput("Введення рівня рекурсії", "Вкажіть рівень рекурсії:", minval=1, maxval=15))

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, 100, level)

    # Закінчення роботи
    screen.mainloop()


if __name__ == "__main__":
    main()
