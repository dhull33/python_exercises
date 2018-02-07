#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:55:34 2018

@author: davidhull
"""

# Uppercase a string
x = 'p'
print(x.upper())

# Capitalize a string
x = "david"
print(x.capitalize())

# Reverse a string

rev = x[::-1]
print(rev)
    
# Leetspeak

def leet():
    x = input("What's your giant string? ")
    k = list(x.lower())
    final = []
    for i in range(len(k)):
        if k[i] == "a":
            k[i]= '4'
            
        elif k[i] == 'e':
            k[i] = '3'
        
        elif k[i] == 'g':
            k[i] = '6'
            
        elif k[i] == 'i':
            k[i] = '1'
            
        elif k[i] == 'o':
            k[i] = '0'
        
        elif k[i] == 's':
            k[i] = '5'
            
        elif k[i] == 't':
            k[i] = '7'
            

        final += k[i] 
    
    fin = ''.join(map(str, final))
    return fin




# Long-Long Vowels
def add_vowels():
    x = input("Give me your word: ")
    vowels = ['aa', 'ee', 'ii', 'oo', 'uu', 'AA', 'EE', 'II', 'OO', 'UU']
    
    fin = ''
    for i in range(len(x)):
        
        if x[i:i+2] in vowels:
            fin += x[i] * 4
        else:
            fin += x[i]
    return fin
        
        
# Caesar Cipher 

def ceasar_cipher():
    
    init = input("What shall I encrypt for you good? ")
    unencr = init.lower()
    
    encr = ''
    for i in range(len(unencr)):
        if ord(unencr[i]) <= 109:
           num = ord(unencr[i])
           n_num = num + 13
           encr += chr(n_num)
           
        elif ord(unencr[i]) >= 110:
            num = ord(unencr[i])
            n_num = num - 13
            encr += chr(n_num)
        
        else:
            encr += unencr[i]
    return encr
            
            
       




