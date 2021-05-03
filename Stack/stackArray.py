# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:36:36 2021

@author: Aditi Devgan
"""

class Stack():
    def __init__(self,size):
        self.stack = []
        self.top = -1
        self.size = size
    
    def peek(self):
        if self.top == None:
            print("No value available!")
        else:
            return self.stack[self.top]
    
    def push(self,item):
        if self.size == self.size-1:
            print("No value can be inserted!")
        else:
            self.stack.append(item)
            return self.stack
    
    def pop(self):
        if self.size == None:
            print("NO value can be poped!")
        else:
            self.stack.pop()
            return self.stack
        
myStack = Stack(5)
myStack.push(2)
myStack.push(3)
myStack.push(5)
v1 = myStack.pop()
myStack.pop()
#myStack.push(8)
print(myStack.peek())
myStack.push(2)
myStack.push(5)
print(myStack.stack)