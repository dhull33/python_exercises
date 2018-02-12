#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:11:04 2018

@author: davidhull
"""

import turtle

from turtle import *

def pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.right(72)
    mainloop()