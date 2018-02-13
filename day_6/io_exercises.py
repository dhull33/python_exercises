#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:29:29 2018

@author: davidhull
"""
file_handle = open('zeus.txt', 'w')
file_handle.write('Hey. Get a job.\n')
file_handle.close()
### Exercise 1 ### 

def file_read():
    file_handle = input("Please enter file name: ")
    
    with open(file_handle, 'r') as fh:
        contents = fh.read()
        print(contents)

### Exercise 2 ###
def file_write():
    file_handle = input('Please enter file name: ')
    
    contents = input('Whatcha you wanna put in it? ')
    
    with open(file_handle, 'w') as fh:
        fh.write(contents)
    

### Exercise 3 ###

def strip_punc(s):
    from string import punctuation
    
    return ''.join(c for c in s if c not in punctuation)

# Letter Summary #
def let_hist(x):
    x = strip_punc(x).lower()
    
    letters = {}
    
    for char in x:
        in_let = letters.get(char, "None")
        
        if in_let == "None":
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
    
# Word Summary #

def word_hist(x):
    x = x.lower()
    
    xlist = strip_punc(x).split()
    
    words = {}
    
    for word in xlist:
        in_word = words.get(word, "None")
        
        if in_word == "None":
            words[word] = 1
        else:
            words[word] += 1
    return words


def let_word():
    file_handle = input("Please enter file name: ")
    
    with open(file_handle, 'r') as fh:
        contents = fh.read()
        return (let_hist(contents), word_hist(contents))



### Exercise 4 ###

import json 

dat = {
  "data": [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
  ]
}

with open('da.json', 'w') as fh:
    json.dump(dat, fh)

def plot():
    import matplotlib
    import matplotlib.pyplot as plt
    import pandas as pd
    
    file_handle = input("Please enter your JSON file: ")
    
    with open(file_handle, 'r') as fh: 
        
        data = json.load(fh)
        df = pd.DataFrame(data)
        df.plot("data")
        print(df)
    
    

with open('da.json', 'r') as fh:
    contents =json.load(fh)
    print(contents)
    print(type(contents))
    contents['data'][1][1]
    
    df = pd.DataFrame(contents)
    df.index
    print(df)
    
    print(df["data"][0][0])



pd_series = pd.Series(dat)
pd_series[0][0]
pd_series[0][0][0]





















