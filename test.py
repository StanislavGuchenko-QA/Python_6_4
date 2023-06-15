from math import pi
import random

def test_greeting():
    name = "Анна"
    age = "25"
    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60
    area = a * b
    assert area == 200

