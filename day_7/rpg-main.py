#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:22:46 2018

@author: davidhull
"""
from hero_rpg import *

hero = Hero()
goblin = Goblin()
zombie = Zombie()
goblin.alive()
hero.alive()
hero.alive

while hero.alive() and zombie.alive():
    print('You have {} health and {} power.'.format(hero.health, hero.power))
    print('The zombie has {} health and {} power.'.format(zombie.health, zombie.power))
    print()
    print('What would you like to do?')
    print('1: Fight that motherfucker')
    print('2: Stand there like a brain dead turd')
    print('3. Bitch out')
    print('>', end = ' ')
    
    raw_input = int(input())
    
    if raw_input == 1:
        # Hero fights goblin
        print("Prepare to meet your doom zombie!")
        
        hero.attack(zombie)
        print("")
        print("You did {} damage to the zombie! Fuck yeah!".format(hero.power))
        zombie.never_die
        print("")
        
        if not zombie.alive():
            print("You have defeated the goblin!!\nThe realm is finally at peace thanks to your bravery.")
        
          
        
            
    elif raw_input == 2:
        pass
    
    
    elif raw_input == 3:
        print("You have brought shame upon your family.")
        break
    
    else:
        print("Invalid input {}".format(raw_input))
        break
    
    
    if zombie.alive():
        print("I AM COMING FOR YOU HERO!!!!! --ZomZom")
        zombie.attack(hero)
        print('')
        print('The zombie has taken {} health from you hero.'.format(zombie.power))
        zombie.never_die()
        
        if hero.alive():
            pass
        else:
            print("You are a disgrace.")