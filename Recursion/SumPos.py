# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:17:18 2021

@author: Aditi Devgan
"""

n = int(input())
def SumPos(n):
    if n<0:
        print("Only positive numbers can be inserted!")
    elif n==0:
        return 0
    else:
        return int(n%10) + SumPos(int(n/10))

print(SumPos(n))
    