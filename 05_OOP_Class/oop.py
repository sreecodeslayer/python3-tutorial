'''
Python Class and OOP Concepts
=============================
Python has been an object-oriented language since it existed.
In python, we consider everything as objects/entity of real world

An object has two characteristics:
    attributes
    behavior

Parrot is an object,

    name, age, color are attributes
    singing, dancing are behavior


Basic OOP Concepts:
------------------
Inheritance:
Using details from a class inside another. Just like a child inherits their parents
and ancestors

Encapsulation / Abstraction:
Showing only what has to be show to other classes and objects, while hiding 
implementation and private details.

Polymorphism:
Multiple usage of an operation in different circumstances of data input.

'''

'''
Python Class
------------
A class in python is like a structural exlanation of the underlying object it tries
to create programmatically.
We can call it as a blueprint to the object.

We can think of class as an sketch of a parrot with labels.
It contains all the details about the name, colors, size etc.
Based on these descriptions, we can study about the parrot. 

like so, in Python

class Parrot:
	pass

is a simple Parrot class with no attributes and behaviours defined yet.
'''
'''
Python Object
-------------
An object is an instance of class.
Untill we create an object of the class, no memory is allocated. Only the description
of the class is stored by Python.


robin = Parrot()

where robin is a parrot (an object of class Parrot)
'''

'''
1. Defining a simple class
==========================
'''


class Parrot:
    species = 'bird'
    legs = 2
    wings = 2
    eyes = 2
    feathers = True

    def __init__(self, name, color):
        self.name = name
        self.color = color


robin = Parrot('robin', 'blue')
print(robin)


'''
The print statement prints out a weird memory location like
<__main__.Parrot object at 0x7f182c0dcb38>

We can tell python what to print when we ask for representaton of the object
using __repr__() of the class

    def __repr__(self):
        return '<Parrot %s %s>' % (self.name, self.color)

'''


class Parrot:
    species = 'bird'
    legs = 2
    wings = 2
    eyes = 2
    feathers = True

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return '<Parrot: %s %s>' % (self.name, self.color)


robin = Parrot('robin', 'blue')
print(robin)

'''
2. Defining behaviour
=====================

'''


class Parrot:
    species = 'bird'
    legs = 2
    wings = 2
    eyes = 2
    feathers = True

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return '<Parrot: %s %s>' % (self.name, self.color)

    def fly(self):
        print('Preparing wings')
        print('Crouching...')
        print('Jumping...')
        print('%s is now flying...' % self.name.capitalize())

    def sit(self):
        print('Slowing down..')
        print('Descending...')
        print('Hops on to a branch...')
        print('%s has landed on a tree branch' % self.name.capitalize())


'''
3. Properties and Attributes
============================
@property 
'''


class Parrot:
    species = 'bird'
    legs = 2
    wings = 2
    eyes = 2
    feathers = True

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self._is_flying = False

    def __repr__(self):
        return '<Parrot: %s %s>' % (self.name, self.color)

    def fly(self):
        print('Preparing wings')
        print('Crouching...')
        print('Jumping...')
        print('%s is now flying...' % self.name.capitalize())
        self._is_flying = True

    def sit(self):
        print('Slowing down..')
        print('Descending...')
        print('Hops on to a branch...')
        print('%s has landed on a tree branch' % self.name.capitalize())
        self._is_flying = False

    @property
    def is_flying(self):
        return self._is_flying

    @property
    def is_sitting(self):
        return not self._is_flying


'''
4. Inheritanc
=============
'''


class Bird:
    species = 'bird'
    legs = 2
    wings = 2
    eyes = 2
    feathers = True

    def fly(self):
        pass

    def sit(self):
        pass


class Parrot(Bird):

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self._is_flying = False

    def __repr__(self):
        return '<Parrot: %s %s>' % (self.name, self.color)

    def fly(self):
        print('Preparing wings')
        print('Crouching...')
        print('Jumping...')
        print('%s is now flying...' % self.name.capitalize())
        self._is_flying = True

    def sit(self):
        print('Slowing down..')
        print('Descending...')
        print('Hops on to a branch...')
        print('%s has landed on a tree branch' % self.name.capitalize())
        self._is_flying = False

    @property
    def is_flying(self):
        return self._is_flying

    @property
    def is_sitting(self):
        return not self._is_flying
