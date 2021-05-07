# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:33:18 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
n = len(arr)
for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j >=0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = temp

print(*arr)