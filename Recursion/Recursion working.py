# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:26:22 2021

@author: Aditi Devgan
"""

n = int(input())
def RecursionMethod(n):
    if n<1:
        print("The number is less than 1!")
    else:
        RecursionMethod(n-1)
        print(n)

print(RecursionMethod(n))