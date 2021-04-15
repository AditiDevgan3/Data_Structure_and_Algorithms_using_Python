# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:05:36 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
val = int(input())
def FindNum(arr,val):
    if val in arr:
        return "Value found!"
    else:
        return "Value not found!"

print(FindNum(arr, val))
    