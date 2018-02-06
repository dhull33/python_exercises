#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:14:22 2018

@author: davidhull
"""

### Sum the numbers ###
list1 = [1,2,3,49,3, 10, 9]

sumsum = sum(list)
print(sumsum)

## Find the largest number
print(max(list1))

min(list1)

#Print each even number in list

for i in list1:
    if i % 2 == 0:
        print(i)
        
# Print positive numbers 

list2 = [-2, -34, 32, 9, 90, -105, 2, 45, 27, -9]

for i in list2:
    if i > 0: 
        print(i)
        
# Create a new list with positive numbers
positive = []
for i in list2:   
    if i > 0:
        positive.append(i)

print(positive)

#Multiply a list

mult = list2 * 9
print(mult)

# Multiplying vectors element wise

vec1 = [2,4,5]
vec2 = [2,3,6]

vectors2 = []
for i in range(0, 3):
    x = vec1[i] * vec2[i]
    vectors2.append(x)

print(vectors2)

# Adding Matrices

mat1 = [[1,3,2], [2,4,9]]
mat2 = [[5,2,67], [1,0,5]]

bmat = []

for i in range(len(mat1)):
    vec = []
    for j in range(len(mat1[i])):
        x = mat1[i][j] + mat2[i][j]
        vec.append(x)
    bmat.append(vec)
    
print(bmat)

len(mat1)

 # Adding 2 matrices of any size as long as they are the same size

def add_matrices (x, y):
    if len(x) != len(y):
        raise ValueError("Matrices must be of the same size")
    
    bmat = []
    for i in range(len(x)):
        if len(x[i]) != len(y[i]):
            raise ValueError("You done fucked up son")
            
        vec =[]
        for j in range(len(x[i])):
                z = x[i][j] + y[i][j]
                vec.append(z)
        bmat.append(vec)
    return(bmat)
()        
    
add_matrices(mat1, mat2)


# Remove duplicates from a list of numbers of a list of strings

def rdup(x):
    
    if len(x) == 1:
        return x
    elif type(x[0]) == 'str':
        new = [i.lower() for i in x]
        
        new = sorted(x)
        z = 0 
        while z < len(x):
            if new[z] == new[z+1]:
                new.pop(new[z])
                z+=1
        
    
    else:
        new = sorted(x)
        z = 0
        while z < len(x):
            if new[z] == new[z+1]:
                new.pop(new[z])
                z+=1
         
    return new
    
               
        
                 
 
                
rdup(x=[1,2,1,4,9,6,1])











        


