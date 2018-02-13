#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:08:20 2018

@author: davidhull
"""

import turtle
from turtle import *



def triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.right(120)
    mainloop()





def square():
    shape("turtle")
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



def pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.right(72)
    mainloop()
    
   

def hexagon():
    for i in range(6):
        turtle.forward(95)
        turtle.right(60)
    mainloop()
    
def octagon():
    for i in range(8):
        turtle.forward(120)
        turtle.right(45)
    mainloop()
    
    
    
def star():
    for i in range(5):
        forward(100)
        right(144)
        
    mainloop()
    

def og_circle():
    width(10)
    circle(180)
    
    mainloop()


    