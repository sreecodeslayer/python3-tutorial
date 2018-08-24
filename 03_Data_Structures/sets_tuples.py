'''
===========
Python Set
===========
A Set is an unordered collection data type that is iterable,
mutable, and has "no duplicate" elements.

Mathematical equivalent.
'''
people = {"Jay", "Karan", "Arjun"}

'''
1. Adding members
=================
.add() instead of .append()
'''
people.add("Daxit")

'''
2. Union, Intersection, Difference
'''
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}

population = people.union(vampires)
population = people | vampires

victims = people.intersection(vampires)
victims = people & vampires

safe = people.difference(vampires)
safe = people - vampires
