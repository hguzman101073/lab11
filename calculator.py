# https://github.com/hguzman101073/lab11
# I, Joseph Menzo, am partner 2
# Henry Guzmans and Joseph Menzos Git Code for calculator.py
import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        return "Error: division by zero"


def logarithm(a, b):
    try:
        if a == 1:
            raise ZeroDivisionError
        elif b <= 0:
            raise ValueError("Input must be greater than 0")
        elif a <= 0:
            raise ValueError("a must be positive")
        return math.log(b, a)  # use math library + raise ValueError
    except ZeroDivisionError:
        return "a can't be 1"
    except ValueError:
        return "value error"


def exp(a, b):
    return a ** b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def exponent(a, b):
    return a ** b


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Error: Cannot calculate of a negative number")


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("The first number a cannot be 0")
    return b / a


def exponent(a, b):
    return a ** b