"""
Dictionary Exercises: 12-Feb-18
"""

### Exercise 1 ###

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# Print elizabeth's number
print(phonebook_dict['Elizabeth'])

# Add entry
phonebook_dict['Kareem'] = '938-489-1234'

# Delete entry
del phonebook_dict['Alice']

# edit an entry 
phonebook_dict['Bob'] = '968-345-2345'

#print all phone entries
for name, number in phonebook_dict.items():
    print(name, number)


### Exercise 2 - Nested Dictionaries ###
ramit = {
        'name': 'Ramit',
        'email': 'ramit@gmail.com',
        'interests': ['movies', 'tennis'],
        'friends': [
            {
                'name': 'Jasmine',
                'email': 'jasmine@yahoo.com',
                'interests': ['photography', 'tennis']
                },
            {
                'name': 'Jan',
                'email': 'jan@hotmail.com',
                'interests': ['movies', 'tv']
                }
            ]
        }   

# Get Ramit's email address

ramit_email = ramit['email']

# Get first of ramit's interest
ram_int1 = ramit['interests'][0]

# Get Jasmine's email address
jas_email = ramit['friends'][0]['email']

# 2nd Jan interest
jan_int2 = ramit['friends'][1]['interests'][1]


### Letter Summary ###
def let_hist():
    x = input("Feed me your word: ").lower()
    
    letters = {}
    

    for char in x:
        in_let = letters.get(char, "None")
        
        if in_let == "None":
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
    
    
    
    
    
    
### Word Summary ###
def strip_punc(s):
    from string import punctuation
    
    return ''.join(c for c in s if c not in punctuation)

def word_hist():
    x = input("Please insert your paragraph: ").lower()
    
    xlist = strip_punc(x).split()
    
    words = {}
    
    for word in xlist:
        in_word = words.get(word, "None")
        
        if in_word == "None":
            words[word] = 1
        else:
            words[word] += 1
    return words
    
    
    
    
    
    
    
    
    
    
    
    