# Joseph Menzo Git Code
import unittest
from calculator import *

def test_add():
    assertEqual(add(5,6), add(6,5))
    assertEqual(add(-25,0), -25)
    assertEqual(add(100, -2000), -1900)
    #assertEqual(add(1.5,2.3), 3.8)

def test_subtract():
    assertEqual(sub(5, 6), -1*sub(6, 5))
    assertEqual(sub(0, 6), -6)
    assertEqual(sub(0, 0), 0)

def test_divide_by_zero():
    assertEqual(div(0,5), "Error: division by zero")

def test_logarithm():
    assertEqual(log(2,8),3)
    assertEqual(log(10,100), 2)
    assertEqual(log(2, 0.5), -1)

def test_log_invalid_base():
    assertEqual(log(1, 5), "a can't be 1")
    assertEqual(log(-5, 25), "a must be positive")
