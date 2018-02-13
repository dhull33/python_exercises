#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:49:12 2018

@author: davidhull
"""

class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        print('You have {} health and {} power.'.format(self.health, self.power))
    
    def attack(self, enemy):
        enemy.health -= self.power


       
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
           

class Goblin(Character): 
    def __init__(self):
        self.health = 6
        self.power = 2
    
    
    
    
        
    
    



hero = Hero()
goblin = Goblin()
goblin.alive()
hero.alive()
hero.alive

while hero.alive() and goblin.alive():
    print('You have {} health and {} power.'.format(hero.health, hero.power))
    print('The goblin has {} health and {} power.'.format(goblin.health, goblin.power))
    print()
    print('What would you like to do?')
    print('1: Fight that motherfucker')
    print('2: Stand there like a brain dead turd')
    print('3. Bitch out')
    print('>', end = ' ')
    
    raw_input = int(input())
    
    if raw_input == 1:
        # Hero fights goblin
        print("Prepare to meet your doom goblin!")
        
        hero.attack(goblin)
        print("")
        print("You did {} damage to the goblin!".format(hero.power))
        
        if not goblin.alive():
            print("You have defeated the goblin!!\nThe realm is finally at peace thanks to your bravery.")
        
          
        
            
    elif raw_input == 2:
        pass
    
    
    elif raw_input == 3:
        print("You have brought shame upon your family.")
        break
    
    else:
        print("Invalid input {}".format(raw_input))
        break
    
    
    if goblin.alive():
        print("I AM COMING FOR YOU HERO!!!!! --GobGob")
        goblin.attack(hero)
        print('')
        print('The goblin has taken {} health from you hero.'.format(goblin.power))
        
        if hero.alive():
            pass
        else:
            print("You are a disgrace.")
        
    
            

    
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
