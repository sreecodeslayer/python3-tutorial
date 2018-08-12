'''
======================
User inputs in Python
======================

We will use this file to write a simple program that
let's user feed data to program
'''

# print("Hello user,")
# name = input("What can I call you?\n")
# age = int(input("How old are you?\n"))
# print("Hi %s, you are going to be %s next year" % (name, age+1))
# print("You just earned stars!")
# print('*'*age)

"""
Well you can go creative with this function, and do many things
from calculating how long the name is to building a biodata for the user.
It is all upto you, but to do those we need to learn more.

So once  you have learnt the basics of python,
you can come back to this file and
add up features to the small program, go crazy.
"""

"""
Let us see what happens if the user gave a wrong input for age.
Like the user said 'Twenty One'.
This ofcourse is a valid age when seen as and English statement.
But we told python to interpret
the input as an integer, but 'Twenty One' is not a valid integer.
"""
"""
Python lets us hanlde unexpected/expected error without
letting the program die.
try:
	.
	.
	.
except TheUnwantedExpectionClass:
	.
	.
	.
	Let know user of needed,
	gracefully hanlde the error

Here the place where the error can occur is while python interprets
the line No. 11
Let's wrap it inside a try/except.
"""

# print("Hello user,")
# name = input("What can I call you?\n")
# try:
#     age = int(input("How old are you?\n"))
# except ValueError:
#     try:
#         age = int(input("How old are you (in numerics)?\n"))
#     except ValueError:
#         age = int(input("How old are you (in numerics, eg. 21)?\n"))

# print("Hi %s, you are going to be %s next year" % (name, age+1))
# print("You just earned stars!")
# print('*'*age)
