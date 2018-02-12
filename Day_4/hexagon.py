#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:16:14 2018

@author: davidhull
"""

import turtle

from turtle import *

def hexagon():
    for i in range(6):
        turtle.forward(95)
        turtle.right(60)
    mainloop()