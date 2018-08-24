'''
===================
Python Dictionaries
===================
Like a list, a dictionary is a collection of many values.
But unlike indexes for lists, indexes for dictionaries
can use many different data types, not just integers.
Indexes for dictionaries are called keys,
and a key with its associated value is called a key-value pair
'''
# spam = {'egg': 2, 'color': 'white', 'price': 11.00}

'''
1. Ordering
===========
Unlike lists, dictionaries are unordered
'''
# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# print('spam == bacon : ', spam == bacon)

# eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
# ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
# print('eggs == ham : ', eggs == ham)

'''
2. Accessing unavailable key
============================
Just like IndexError in lists, accessing an invalid key from 
a dictionary result in KeyError
'''
# spam = {'name': 'Zophie', 'age': 7}
# print(spam['color'])

'''
3. Keys, Values and Items
=========================
A dictionary can be split into keys, values, and items as a whole.
keys : list(dict_keys) of all available keys in dictionary
values : list(dict_values) of all values of keys in dictionary
items : list(dict_items) of tuple (key,value) in dictionary
'''
# car = {'color': 'red', 'wheels': 4, 'type': 'sedan'}
# print('Properties of car: ', car.keys())
# print('Properties given to this car: ', car.values())
# print('Car: ', car.items())

'''
4. get() or return default
==========================
the get method for dictionaries returns the value of the key if present.
The method by default returns NoneType if there is no key which was specified.
This can be changed to the value we need by default.
This is one of the handiest function that we mostly use in cases of dictionary
operations.
'''
# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing %d Apples and %d Cups for picnic' %
#       (picnicItems.get('apples', 0), picnicItems.get('cups', 0)))
# print('I am bringing %d Eggs' % picnicItems.get('eggs', 0))

'''
If we were not to use the get method to obtain the values, python would raise
the KeyError upon using the Bracket method or the index based approach.

This is not wrong, but we will have to wrap the Try/Except on each access that
we try to do.
Both approach have their own use, which we will understand a bit later while 
developing some applications.

Let's see
'''
# print(picnicItems['eggs'])
# try:
#     print(picnicItems['eggs'])
# except KeyError:
#     print(0)
