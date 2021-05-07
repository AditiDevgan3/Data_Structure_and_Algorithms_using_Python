# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:55:55 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
n = len(arr)
for i in range(0,n-1):
    min_val = i
    for j in range(i+1,n):
        if arr[j] < arr[min_val]:
            min_val = j
    
    if min_val != i:
        arr[i],arr[min_val] = arr[min_val],arr[i]

print(*arr)