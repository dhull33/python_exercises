#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:11:22 2018

@author: davidhull
"""
### Finding the Nth prime ###
import math

# is_prime checks if n is prime using Wilson's Theorem. Returns true if n is prime and false otherwise. 
def is_prime(n):
    if math.factorial(n-1) % n == -1 % n:
        return True
    else:
        return False
    
def large_prime():
    n = int(input("What's the largest prime you want to know? "))
    
    prim = 5
    a = [2,3]
    
    if n == 1:
        return 2
    
    elif n == 2:
        return 3
    
    else:
        while len(a) < n: 
            
            if is_prime(prim) == True:
                a.append(prim)
                
            prim += 2
                
    return a[-1]




### Algo 1 ###
def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

### Algo 2 ###
def sum_531000():
    add = 0
    
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            add += i
        else:
            continue 
    return add





### Algo 3 ###
def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def add_fib():
    add = 0
    
    for i in range(1, 4000001):
        
        if fib(i) > 4000000:
            break

        elif fib(i) % 2 == 0:
            add += fib(i)
    return add






### Algo 4 ###
def trial_division(n):
    a = []  
    while n%2 == 0:
        a.append(2)
        n/=2
    f=3
    while n > 1:
        if (n % f == 0):
            a.append(f)
            n /= f
        else:
            f += 2             
    return max(a)

        
 

        
  
    
    
        
    
