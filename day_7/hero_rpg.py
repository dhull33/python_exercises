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

class Zombie(Character):
    def __init__(self):
        self.health = 100
        self.power = 1
    
    def never_die(self):
        self.health += 6
    
    
        
    
            

    
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
