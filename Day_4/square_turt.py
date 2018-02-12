#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:06:18 2018

@author: davidhull
"""

from turtle import *

def squared():
    
    #move into position
    up()
    forward(50)
    left(90)
    forward(50)
    left(90)
    
    down()
    
    # draw the square
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

    mainloop()