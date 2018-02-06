#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:30:51 2018

@author: davidhull
"""

### While Loops ###
count = 0

while count < 10:
    count +=1
    print("The count is", count)
    
print("You is done!")

## Checking input ##
answer = ''

while answer != 'when':
  answer = input('Say when: ')
  answer = answer.lower()
print("Cheese")

## breaks in While loops

while True:
    answer = input("Say when: ")
    if answer.lower() == 'when':
        break
print("Cheese")