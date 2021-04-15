# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:11:30 2021

@author: Aditi Devgan
"""

arr = list(map(int,input().split()))
index = int(input())
def find(arr,index):
    if index >= len(arr):
        return "Wrong value inserted!"
    else:
        return arr[index]

print(find(arr,index))
    