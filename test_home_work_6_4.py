import math
import random


def test_greeting():
    name = "Анна"
    age = "25"
    # Вывод строки с приветствием
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
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
    # Cоздание списка из 10 случайных чисел в диапазоне от о 1 до 100
    l = []
    for x in range(10):
        l.append(random.randint(1,100))
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # Удаление из списка повторяющихся элементов
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # Создание словаря и вывод результата
    d = dict(zip(first, second))
    print(d.values())
    assert isinstance(d, dict)
    assert len(d) == 5