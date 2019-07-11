#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/04_2_fibonacci.py

def fibonacci(n): #definicja funkcji
    pwyrazy = (0, 1) #dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy #przypisanie wielokrotne, rozpakowanie tupli
    while n > 0:
        print (b)
        a, b = b, a+b #przypisanie wielokrotne
        n -= 1

n = int(input("Podaj numer wyrazu: "))
fibonacci(n)
print ("")
print ("=" * 20)

def fibonacci2(n):
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while a < n:
        a, b = b, a+b
    print (a)

fibonacci2(n)
