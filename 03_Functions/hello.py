'''
================
Python Functions 
================

Functions in python like almost all programming languages
lets the programmer group certain related tasks into a single 
function call.
Functions change the flow of control just like the loops and
the conditional statements that learned a while ago.

Functions help programmer remove code duplication.

def function():
    pass

'''


def hello(times):
    '''
    hello prints out the string 'Hello!' the number of times
    its asked to line by line.
    This function takes one required variable (positional argument)
    '''
    print('Hello! \n' * times)
