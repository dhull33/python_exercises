#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:08:20 2018

@author: davidhull
"""

from turtle import *
import turtle
 

def triangle():
   
    for i in range(3):
        forward(100)
        right(120)
    





def square():
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

    



def pentagon():
    
    for i in range(5):
        turtle.forward(100)
        turtle.right(72)
    
  
   

def hexagon():
    
    for i in range(6):
        turtle.forward(95)
        turtle.right(60)
 
    
def octagon():
    
    for i in range(8):
        turtle.forward(120)
        turtle.right(45)
    
 
    
    
def star():
    
    for i in range(5):
        forward(100)
        right(144)
        
    
    

def og_circle():
    
    width(3)
    circle(180)
    
    


    