#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:32:56 2018

@author: davidhull
"""

import sys

sys.stdout.write("Hello World\n" "Big Poppa")

"""
Three quotes allow me to type on multiple lines without having to keep using # over and over again 
"""
""" 
String Formatting
"""
first = "David"
last = "Hull"

#By Argument 

"Hello {} {}".format(first, last)

#By index

"Hello {0} {1}, again {0}".format(last, first)

# By keyword

"Hello {first} {last}, again {first}".format(first="James", last = "Bond")

# USing input() 

first = input("First name: ")

last = input("Last name: ")


count = 0
while count < 10:
    count += 1
    print("The count is", count)
    
print("You is finished!!")
    