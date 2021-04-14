# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:03:24 2021

@author: Aditi Devgan
"""

n = int(input())
def fib(n):
    if n==1 or n==2:
        return 1
    elif n==0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))