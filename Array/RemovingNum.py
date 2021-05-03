# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:21:08 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
val = int(input())
def FindNum(arr,val):
    if val in arr:
        arr.remove(val)
        return arr
    else:
        return "Value not found!"

print(FindNum(arr, val))