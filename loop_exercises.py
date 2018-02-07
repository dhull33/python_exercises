#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:38:58 2018

@author: davidhull
"""

# 1 to 10

for i in range(1,11):
    print(i)


# n to m

start = int(input('WHat integer should I start at? '))  

end = int(input('What integer should I end at? '))

for i in range(start, end + 1):
    print(i)
  
    
# Print odd numbers 1-10

for i in range(1, 11):
    if i % 2 != 0:
        print(i)
    else:
        pass
    
    
# Print a 5x5 square of * characters
for i in range(5):
    print('*'*5)
    
    
# Print an nxn square of * characters

def square():
    n = int(input("How big is the square? "))
    
    for i in range(n):
        print('*' * n)
        

# Print an n x m box
def box():
    width = int(input("Width? "))
    height = int(input('Height? '))
    
    inner_width = width - 2
    inner_height = height - 2
    
    print('*' * width)
    for i in range(inner_height):
        print('*' + ' ' * inner_width + '*' )
    print('*' * width)
    
    
# Print a triangle of *  characters 
height = 4
for i in range(1,5):
    print(' '*(height - i) + '*' * (i+(i-1)) + ' '*(height-i))


# Print a triangle of height n with * characters
def triangle():
    height = int(input('How big of a triangle do you want? '))
    
    for i in range(1,height + 1):
        print(' '*(height - i) + '*' * (i+(i-1)) + ' '*(height-i))
    


# Print Multiplication table for numbers 1-10

for i in range(1,11):
    for j in range(1,11):
        print(i,'X' ,j ,'=', i*j)





