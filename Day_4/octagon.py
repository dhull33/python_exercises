#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:26:28 2018

@author: davidhull
"""

import turtle

from turtle import * 

def octagon():
    for i in range(8):
        turtle.forward(120)
        turtle.right(45)
    mainloop()