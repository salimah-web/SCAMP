# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:10:23 2020

@author: salima omari
"""


'''the fibonacci sequence is a series of numbers in which the numbers are
gotten from addtion of the two previous numbers'''
a=0 # taking 0 as the first number 
b=1 # and 1 as the second number
fib_nums=[]
user_input=int(input('how many fibonnacci sequence do you want?\n>>>'))
for i in range(user_input):
    a,b=b,a+b
    fib_nums.append(a)
print(f'the first {user_input} fibonacci sequence is {fib_nums}')