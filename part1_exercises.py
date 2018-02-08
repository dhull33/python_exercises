#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:08:49 2018

@author: davidhull
"""

# Hello, you!
name = input('What is your name? ') 
print("Hello, {}!".format(name))

#Hello, you capitalized
name = input('What is your name? ')
length = len(name)
name = name.upper()
print("HELLO, {}!\nYOUR NAME HAS {} LETTERS IN IT! AWESOME".format(name, length))

#Madlib 
print("Please fill in the blanks below: \n____(name)____'s favorite subject in school is ____(subject)____.")
name = input("What is name? ")
subject = input('What is subject? ')
print("{}'s favorite subject in school is {}.".format(name, subject))

# Day of the Week

def week():
    day = int(input("What day of the week is it (0-6)? "))
    
    if day == 0:
        return 'Sunday'
    elif day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Wednesday'
    elif day == 4:
        return 'Thursday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    else:
        raise ValueError("That shit wrong!")
        

# Work or sleep in?
def work_week():
    day = int(input("Do I sleep or do I work (0-6)? "))
    
    if day in range(1,6):
        print("Go to work :'( ")
    elif day == 0 or day == 6:
        print("Sleep in!")
    else:
        print("Get your shit straight")
   
# Celsius to Fahrenheit

def fahr():
    temp = int(input("What is the temperature in Celsius? "))
    
    print((temp * 1.8) + 32, "F")
    
#Tip Calculator
def tip(): 
    bill = float(input("Total bill amount: "))
    lev_serv = input("Level of service (good, fair, or bad)? ")
    lev_serv = lev_serv.lower()
    
     
    if lev_serv == "good":
        tip = bill * 0.20
        tot_bill = tip + bill
        print("Tip amount: {:.2f}\nTotal amount: {:.2f}".format(tip, tot_bill))
    
    elif lev_serv == "fair":
        tip = bill * 0.15
        tot_bill = tip + bill
        print("Tip amount: {:.2f}\nTotal amount: {:.2f}".format(tip, tot_bill))
    elif lev_serv == 'bad':
        tip = bill * 0.10
        tot_bill = tip + bill
        print("Tip amount: {:.2f}\nTotal amount: {:.2f}".format(tip, tot_bill))
    
    else:
        raise ValueError("You done messed up")
        
        
# Tip Calculator #2
#Tip Calculator
def tip2(): 
    bill = float(input("Total bill amount: "))
    lev_serv = input("Level of service (good, fair, or bad)? ")
    split = int(input("Split how many ways? "))
    
    lev_serv = lev_serv.lower()
    
     
    if lev_serv == "good":
        tip = bill * 0.20
        tot_bill = tip + bill
        perper = tot_bill / split
        print("Tip amount: ${:.2f}\nTotal amount: ${:.2f}\nAmount per person: ${:.2f}".format(tip, tot_bill, perper))
    
    elif lev_serv == "fair":
        tip = bill * 0.15
        tot_bill = tip + bill
        perper = tot_bill / split
        
        print("Tip amount: ${:.2f}\nTotal amount: ${:.2f}\nAmount per person: ${:.2f}".format(tip, tot_bill, perper))
        
    elif lev_serv == 'bad':
        tip = bill * 0.10
        tot_bill = tip + bill
        perper = tot_bill / split
        print("Tip amount: ${:.2f}\nTotal amount: ${:.2f}\nAmount per person: ${:.2f}".format(tip, tot_bill, perper))
    
    else:
        raise ValueError("You done messed up")
        

# 1 to 10 using a while loop
 count = 1
 
 while count < 11:
     print(count)
     count += 1


# How many coins?

def coins():

    coin = 0
    x = True
    while x == True:
        yes_no = input("You have {} coin.\nDo you want another? ".format(coin))
        if yes_no == 'yes':
            coin += 1
            
        else:
            print("Fine")
            x = False
             



     
    