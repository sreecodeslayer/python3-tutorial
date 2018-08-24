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
spam = {'egg': 2, 'color': 'white', 'price': 11.00}

'''
1. Ordering
Unlike lists, dictionaries are unordered
===========
'''
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print('spam == bacon : ', spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
print('eggs == ham : ', eggs == ham)
