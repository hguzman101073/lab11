#Henry Guzmans Git Code
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
        return math.log(b,a)# use math library + raise ValueError
    except valueError as e:
        return e


def exp(a, b):
    return a**b

