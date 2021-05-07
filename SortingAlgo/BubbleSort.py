# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:10:46 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
n = len(arr)
for i in range(len(arr)):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
        else:
            continue
print(*arr)