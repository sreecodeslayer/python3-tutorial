'''
===========
Python Set
===========
A Set is an unordered collection data type that is iterable,
mutable, and has "no duplicate" elements.

Mathematical equivalent.
'''
# people = {"Jay", "Karan", "Arjun"}

'''
1. Adding members
=================
.add() instead of .append()
'''
# people.add("Daxit")

'''
2. Union, Intersection, Difference
'''
# people = {"Jay", "Idrish", "Archil"}
# vampires = {"Karan", "Arjun"}

# population = people.union(vampires)
# population = people | vampires

# victims = people.intersection(vampires)
# victims = people & vampires

# safe = people.difference(vampires)
# safe = people - vampires


'''
Python Tuples
=============
Tuples are immutable lists. ie. They do not support item assigments
'''
# tup = (1, 2, 3)

'''
1. Count, Index
===============
You cannot extend or append like we did in List section,
but you can count occurances and get index of items in tuple.
'''
# print('No of 1s : %d' % tup.count(1))
# print('Index of 2 in the tup : ' % tup.index(2))

'''
2. Concatenation
================
You can join two or more tuples
'''
# tup1 = (1, 2, 3, 4)
# tup2 = ('one', 'two', 'three', 'four')

# print(tup1 + tup2)

'''
3. Nesting
==========
Tuple inside Tuple.
Tuple can hold other datta types that we have seen so far.
'''
# print((tup1, tup2))
# print((tup1, tup2, {'something': 'useless'}, ['random', 'list']))

'''
4. Immutable property
=====================
As told earlier, we can't modify the tuple.
Let's see
'''
# tup = (0, 1, 2, 3)
# tup[0] = 4
# print(tup)

'''
TypeError: 'tuple' object does not support item assignment
'''
