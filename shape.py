# Подключаем моудуль для выполнения математических операций
import math


# Создаем класс фигура
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")


# Создаем класс круг
class Circle(Shape):

    # Получаем и присваиваем данные для вычисления радиуса
    def __init__(self, radius):
        self.radius = radius

    # Вычисляет площадь круга по радиусу
    def calculate_area(self):
        if self.radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * self.radius ** 2


# Создаем класс треугольник
class Triangle(Shape):

    # Получаем и присваиваем данные для вычисления треугольника
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Вычисляем площадь треугольника по формуле Герона
    def calculate_area(self):
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (
                    semi_perimeter - self.side3))
        return area

    # Проверяем, является ли треугольник прямоугольным
    def is_right_triangle(self):
        sides = [self.side1, self.side2, self.side3]
        max_side = max(sides)
        sides.remove(max_side)
        if max_side ** 2 == sides[0] ** 2 + sides[1] ** 2:
            return True
        return False


# Запрашиваем у пользователя радиус круга
def get_circle_data():
    radius = float(input("Введите радиус окружности: "))
    return Circle(radius)


# Запрашиваем у пользователя длины сторон треугольника
def get_triangle_data():
    side1 = float(input("Введите длину первой стороны треугольника: "))
    side2 = float(input("Введите длину второй стороны треугольника: "))
    side3 = float(input("Введите длину третьей стороны треугольника: "))
    return Triangle(side1, side2, side3)


# Отправляем запрос пользователю
if __name__ == "__main__":
    print("Возможные варианты:")
    print("1. Вычислить площадь круга по радиусу")
    print("2. Вычислить площадь треугольника по трем сторонам")
    choice = int(input("Выберите подходящий набрав цифру (1 или 2): "))

    if choice == 1:
        shape = get_circle_data()
    elif choice == 2:
        shape = get_triangle_data()
    else:
        print("Invalid choice")

    # Проверяем, является ли треугольник прямоугольным
    if isinstance(shape, Shape):
        print("Площадь:", shape.calculate_area())
        if isinstance(shape, Triangle):
            print("Является ли треугольник прямоугольным?", shape.is_right_triangle())
