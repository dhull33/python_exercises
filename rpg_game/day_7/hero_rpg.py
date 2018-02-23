#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:49:12 2018

@author: davidhull
"""
import random
import time



class Character(object):
    def __init__ (self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
    
    def alive(self):
        return self.health > 0
    
    
    def print_status(self):
        print('{} has {} health and {} power.'.format(self.name, self.health, self.power))
    
    def attack(self, enemy):
        if enemy.armor > 0:
            arm_health = enemy.health + enemy.armor
            arm_health -= self.power
            print('Gangsta')
        else:
            enemy.health -= self.power
            print("The {} attacks {}!".format(self.name, enemy.name))
            print('')




       
class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 3
        self.coins = 10
        self.armor = 0
        self.evade = 0
    
    def attack(self, enemy):
        if random.random() <= 0.2:
            self.power = self.power * 2
            enemy.health -= self.power
        elif self.armor > 0:
            arm_health = self.health + self.armor
            arm_health -= enemy.power
            print('Gangsta')
        super(Hero, self).attack(enemy)
    
    #def evades(self, enemy):
        #if self.evade > 0:
            

        
    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)
    
    def restore(self):
        self.health =10
        print("Hero's health is restored to {}!".format(self.health))
        time.sleep(1)

class Goblin(Character): 
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5
        self.armor = 0

class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 100
        self.power = 1
        self.bounty = 10
        self.armor = 0
    
    def attack(self, enemy):
        self.health += 6
        enemy.health -= self.power
        print("The Zombie has taken {} health from you.".format(enemy.health))
        super(Zombie, self).attack(enemy)



    
class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 8
        self.power = random.randint(1,7)
        self.bounty = 6
        self.armor = 0
    
    def attack(self, enemy):
        if random.randrange(1, 10, 1) <= 2:
            self.health += 2
            enemy.health -= self.power
            print("The Medic has gained {} health points!".format(self.health))
            print('')
            print("The Medic has taken {} health from you.".format(enemy.health))
        super(Medic, self).attack(enemy)

    

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = random.randint(0, 9)
        self.count = 0
        self.bounty = 4
        self.armor = 0
        
class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 15
        self.power = random.randint(1, 9)
        self.bounty = 7
        self.armor = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power

        super(Wizard, self).attack(enemy)

class Godzilla(Character):
    def __init__(self):
        self.name = 'Godzilla'
        self.health = 30
        self.power = random.randint(5, 15)
        self.bounty = 25
        self.armor = 0
    
    def attack(self, enemy):
        eat = random.random() > 0.01
        if eat:
            enemy.health -= (self.power * 3)
        super(Godzilla, self).attack(enemy)





###################### Battle ###########################
    
class Thunderdome(object):
    def battle(self, hero, enemy):
        print("==============================")
        print("  Welcome to the Thunderdome  ")
        print("==============================")
        print("            Shhh...\n  ",u"\u2620", "Death is Listening",u"\u2620")
        
        time.sleep(1.5)
        
        print("")
        print("Your Potential Adversaries: \n   The Zombie of Doom \n   The Goblin of Terror \n   The Evil Wizard \n   The Shadow of Death!")
        print("")
        
        time.sleep(1)
        
        print("But Who Would Dare Challenge YOU Hero?!?!?")
        
        
        time.sleep(1)
        
        print("")
        print("The {} challenges you.".format(enemy.name))
        print("")
        print("Do you accept hero (y/n)?")
        yay_nay = input('> ')
        yaynay = yay_nay.lower()
        
        if yaynay == 'y' or yaynay == 'yes':
            pass
        else:
            time.sleep(1)
            print("You disgust me.")
            exit(0)
            
        
        
        while hero.alive() and enemy.alive():
            print("=======================")
            print("Hero faces the {}!".format(enemy.name))
            print("=======================")
            print('')
            hero.print_status()
            enemy.print_status()
            time.sleep(1)
            print('')
            print("-----------------------")
            print("What should you do?")
            print("1. Fight your challenger {}?".format(enemy.name))
            print('2. Do nothing?')
            print('3. Run away?')
            keyinput = int(input("> "))
            
            if keyinput == 1:
                hero.attack(enemy)
                enemy.attack(hero)
            elif keyinput == 2:
                print("Well alrighty then")
                enemy.attack(hero)
            elif keyinput == 3:
                print("You have shamed your family.")
                break
            else:
                print("You are not fit to enter the Thunderdome.")
                break
            
        if hero.alive():
            hero.coins += enemy.bounty
            print("You have defeated {}!".format(enemy.name))
            return True
        else:
            print("You have dishonored your ancestors.")
            return False
        
 



################## Store Items ############################
       
class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))



class SuperTonic(object):
    cost = 15
    name = 'SuperTonic'
    def apply(self, hero):
        hero.health += 10
        print("Hero's health has increased to {}.".format(hero.health))
        
 
       
class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power has increased to {}.".format(hero.name, hero.power))

class Armor(object):
    cost = 3
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2 
        print("Hero's armor has increased to {}!".format(hero.armor))

class Evade(object):
    cost = 12
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2 
        print("You're getting pretty good at dodging attacks.\nYou have {} evade points.".format(hero.evade))


################### Store ############################


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            inp = int(input("> "))
            if inp == 10:
                break

            elif hero.coins < item.cost:
                print("You don't have enough coins dumbass.\nGo back to the Thunderdome and defeat your enemies!")
                print("")
                break
            else:
                ItemToBuy = Store.items[inp - 1]
                item = ItemToBuy()
                hero.buy(item)    
        
        
      



################### Main ###########################

          
        
if __name__ == "__main__":
    hero = Hero()
    
    thunderdome = Thunderdome()
    
    enemies = [Goblin(), Wizard(), Shadow(), Godzilla(), Medic(), Zombie()]
    
    shop = Store()
    
    shame = ["You have brought shame upon your family", "You are a disgrace.", "You are no hero...", "Go back from whence you came you wretched creature!" ]
    for enemy in enemies:
        hero_won = thunderdome.battle(hero, enemy)
        if not hero_won:
            print("What is dead may never die...")
            exit(0)
        shop.do_shopping(hero)
    
    print("Congratulations! You have defeated all your enemies!")
    print("")
    print("What are going to do with all your free time?")
        
   















     
        
        
        
        
        
        
        
