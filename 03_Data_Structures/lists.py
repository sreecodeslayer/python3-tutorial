'''
============
Python Lists
============
Lists as the name suggests helps programmers store collective
values (lsit items) in an order.
[1,2,3] is a list of integers 1,2,3
'''

spam = [1, 2, 3, 4, 5]

'''
Every element in a list have an index, which starts from 0 in Python.
the above list 'spam', the index of value 1 is 0, 2 is 1 and so on
'''

print(spam[0])
print(spam[2])
print(spam[4])
print(spam[1])

'''
In python, trying to access an index which is not assigned
will throw an 'IndexError: list index out of range'
'''

print(spam[7])

'''
1. Extending and Appending
==========================
Extend means to add several items to an existing list
Append means to add one item to the list

Now for common man, this would seem the same. But to Python,
this is two separate methods of the list datatype.

.extend(list)
.append(item)

Extend takes any kind of iterable object in python
that includes list, dict, tuple, set,
However, you can't extend a list with int, str, float as they
are not iterables as per python conventions
'''
other_spams = [8, 7, 6, 9, 10, 2, 1]
spam.extend(other_spams)
other_dict_spams = {'a': 1, 'b': 2}
spam.extend(other_dict_spams)


'''
Well append can also take any kind of python object
that includes a dict, list, tuple, set, int, float, str, 
a custom class object and so on
'''
spam.append(11)
spam.append(12)
spam.append([13, 14])
spam.append(15.6)
spam.append('16')

print(spam)

'''
2. Count and Index of
=====================
.count() lets you count the number of occurance of an item in the list
.index() lets you retrieve index of an item
'''
spam.count('a')
spam.index('a')

'''
3. Length
==========
List also supports the len() we used on strings
It returns the total number of items in the list
'''
print(len(spam))

'''
4. Remove and Pop
=================

.remove(item) will search and remove an item from list
.pop() will take out the last element that was inserted first
and is lost forever.

You can remove and pop untill all elements are out of the list
after which you will get an index error. Try for yourself
'''
spam.remove([13, 14])
spam.remove('16')

spam.pop()

'''
Trying to remove a non-member item will also throw an error
ValueError: list.remove(x): x not in list

'''
spam.remove(100)

'''
5. Reverse and Sort
===================
.reverse() will reverse the order
.sort() will reorder the elements into ascending order by default
'''

spam.reverse()
spam.sort()
spam.sort(reverse=True)

'''
6. List comprehension
=====================
Sometimes there comes a situation where we make a sub list
depending on a satisfaction of some condition

say if the element is greater than a number, we add it to another list instead
'''

initial = [2, 3, 1, 6, 4, 8, 7, 9]
final = []

for item in initial:
    if item > 5:
        final.append(item)
'''
Now there is nothing wrong in writing it this way. However, python
have a way of writing some meaningful one liners that compress a big loop
in to a single line
'''

final = [item for item in initial if item > 5]
final = [item if item > 5 else item*5 for item in initial]
'''
Why list comprehension?
Eventhough the operation looks exactly the same, using list comprehension
to build a list is a bit faster as it uses C directly in building, unlike the for loop in
python that uses append() which makes a numerous function calls, slowing down the flow of
control
'''
