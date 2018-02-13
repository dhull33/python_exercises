#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:20:12 2018

@author: davidhull
"""
import matplotlib.pyplot as plt


def hello(name):
    return "Hello {}".format(name)

# y = x + 1
def f(x):
    return x + 1

def plot():
    xs = list(range(-3, 4))
    ys = []

    for x in xs:
        ys.append(f(x))
    
    plt.plot(xs, ys)
    plt.show()
    
# Plot x^2

def square(x):
    return x**2

def parabola():
    
    
    xs = list(range(-100,101))
    ys = []
    
    for x in xs:
        ys.append(square(x))
    
    plt.plot(xs, ys)
    plt.show()
    
# Odd or Even

def odd_even(x):
    if x % 2 == 0:
        return -1
    else:
        return 1
    
def jailed():
    xs = list(range(-5, 5))
    ys = []
    
    for x in xs:
        ys.append(odd_even(x))
        
    plt.bar(xs, ys)
    plt.show()
    
# Plot sin(x)
import math

def sine(x):
    return math.sin(x)

def plot_sine():
    xs = list(range(-5, 5))
    ys = []
    
    for x in xs:
        ys.append(sine(x))
        
    plt.plot(xs, ys)
    plt.show()


# Plot sin(x) using smaller increments
import numpy as np

def sine2(x):
    return math.sin(x)

def plot_sine2():
    xs = np.arange(-5, 6,0.1)
    ys = []
    
    for x in xs:
        ys.append(sine(x))
        
    plt.plot(xs, ys)
    plt.show()


    
# Plot the temperature
def plot_temp():
    temp = int(input("What is the temperature in Celsius? "))
    
    fahr = temp * 1.8 + 32
    
    xs = np.arange(-50, 120, 0.1)
    ys = np.arange(-50, 120, 0.1)
    
        
    plt.plot(xs, ys, 'b-', fahr, fahr, 'ro')
    plt.text(fahr, fahr, "Your point  ", ha = 'right', weight = 'heavy')
    plt.show()


# Play again
def play_once():
    x = input("Do you want to play again (Y/N)? ")
        
    if x == 'y' or x == "Y":
        return True
        
    elif x == "n" or x == 'N':
        return False
    
    else:
        raise ValueError("Incorrect value")    

# Play again, again
def play():
    try:
        x = input("Do you want to play again (Y/N)? ")
        
        if x == 'y' or x == "Y":
            return True
        
        elif x == "n" or x == 'N':
            return False
    
        else:
            raise ValueError("Incorrect value")
    except:
        
        print("Please enter Y or N")
        
        return play()
        
    
    
    


























