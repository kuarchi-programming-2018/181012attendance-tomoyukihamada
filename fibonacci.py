# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print(fib(2018))