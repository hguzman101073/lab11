#Henry Guzmans and Joseph Menzos Git Code for calculator.py
import math

def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a , b):
    if a == 0:
        raise ZeroDivisionError("The first number a cannot be 0")
    return b / a
def logarithm(a, b):
    if a <=0:
        raise ValueError("Input must be greater than 0")
    return log(b, a)
def exponent(a, b):
    return a**b