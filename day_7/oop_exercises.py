"""
Created on Tue Feb 13 10:04:09 2018

@author: davidhull
"""


### Exercise 1 ###
class Person:
    def __init__ (self, name, email, phone, friends =[], count = 0):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = count
        
    def greet (self, other_person):
        self.count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
    def print_contact_info(self):
        print("{}'s email: {},".format(self.name,self.email), " {}'s phone number: {}".format(self.name, self.phone))
    
    def add_friend(self, friend):
        return self.friends.append(friend)
        
    
    def num_friend(self):
        print(len(self.friends))
    
    def greeting_count(self):
        print("{}".format(self.count))
        
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
    
    #def __str__(self):
        #return "{}".format(self.greeting_count)
    
        
        
        


sonny = Person(name = 'Sonny', email = 'sonny@hotmail.com', phone = '483-485-4948')

jordan = Person(name = 'Jordan', email = 'jordan@aol.com', phone = '495-586-3456')

sonny.greet(jordan)

jordan.greet(sonny)

jordan.greeting_count()
jordan.greet(sonny)
print(sonny.email,"   ", sonny.phone)
print(jordan.email, '   ', jordan.phone)


### Vehicle Exercise ###
class Vehicle:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)
        
car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()





















