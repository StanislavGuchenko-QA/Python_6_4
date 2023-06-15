import math
from math import pi
import random


def test_greeting():
    name = "Анна"
    age = "25"
    # Вывод строки с приветствием
    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20
    # Вычисление периметра прямоугольника
    perimeter = (a + b) * 2
    assert perimeter == 60
    # Вычисление площади прямоугольника
    area = a * b
    assert area == 200


def test_circle():
    # Вычисление площади окружности
    r = 23
    area = math.pi * (r ** 2)
    assert area == 1661.9025137490005

    # Вычесление длины окружности
    length = 2 * math.pi * r
    assert length == 144.51326206513048

def test_random_list():
    # Создание списка из 10 случайных чисел от 1 до 100 и отсортировка его по возрастанию.
    l = random.sample(range(1, 100), 10)
    assert len(l) == 10
    assert l[0] < l[-1]