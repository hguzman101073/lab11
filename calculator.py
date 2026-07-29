#Henry Guzmans and Joseph Menzos Git Code for calculator.py
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return b / a
    except zeroDivisionError:
        return "Error: division by zero"


def log(a, b):
    try:
        if b<=0:
            raise ValueError("b must be positive")
        elif a==1:
            raise ValueError("a can't be 1")
        elif a<=0:
            raise ValueError("a must be positive")
        return math.log(b,a)# use math library + raise ValueError
    except ValueError as e:
        return e


def exp(a, b):
    return a**b

def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def logarithm(a, b):
    if a <=0:
        raise ValueError("Input must be greater than 0")
    return log(b, a)
def exponent(a, b):
    return a**b
