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

A useless function is like the one below

def function():
    pass

'''


# def hello(times):
#     '''
#     hello prints out the string 'Hello!' the number of times
#     its asked to line by line.
#     This function takes one required variable (positional argument)
#     '''
#     print('Hello! \n' * times)


'''
Funtions that returns an output

This function will however fail with a TypeError if we supply values of
types other than a number.
'''


# def divide(numerator: float, denominator: float):
#     try:
#         return numerator / denominator
#     except ZeroDivisionError:
#         print('Cannot divide by zero')
#         return None

'''
Scopes and global variables

Look at the function below and guess what might be the output
before running the code block
'''
# def spam():
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)

# global ghost

# def ghosts():
#     ghost = 15
#     print('Special breed of ghost: ', ghost)


# def anotherghost():
#     print('Am just a plain ghost: ', ghost)


# ghosts()
# anotherghost()
# ghost = 10
# print('Am lonely: ', ghost)

'''
Scopes within functions
'''


# def shop_a():
#     print('** Scope for shop_a created **')
#     veg_burger = 10
#     ham_burger = 20
#     print('We have %s Veg. Burger and %s Ham Burger' %
#           (veg_burger, ham_burger))


# def shop_b():
#     print('** Scope for shop_b created **')
#     veg_burger = 20
#     ham_burger = 10
#     print('We have %s Veg. Burger and %s Ham Burger' %
#           (veg_burger, ham_burger))


# def customer_a():
#     # He visited shop A, so he gets:
#     shop_a()


# def customer_b():
#     # He visited shop A, so he gets:
#     shop_b()


# print('Customer A')
# customer_a()
# print('\nCustomer B')
# customer_b()

# print('\nTrying to access local scopes of shop functions')
# # Obviously python is going to be angry here, let's see
# print(veg_burger, ham_burger)
