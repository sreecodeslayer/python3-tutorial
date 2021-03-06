'''
==================
Strings in Python
==================

We will use this file to write our first string statement in Python
'''

# hello_msg = 'Hello world'

# long_string = "The python string can also be defined using double quotes"

# multiline_string = """The python string also contain multiple lines.
# This is line 1.
# This is line 2.
# By using 'a backward slash' \
# we can tell python to consider what is below as a continuation to \
# the very same line and not to add any tab spacing or new line characters
# And everything is saved onto a single variable"""

'''
Now we can see what all operations we can do with strings and on string

1. Concatenation
================
'''
# first_string = 'Does this string make'
# second_string = 'any sense to any of you sitting here?'
# print(first_string+second_string)

'''
Well that had some issues, let's see what is wrong here to the displayed string
As you can see, python doesn't really care what is the value of string as long as
it follows the allowed characters and syntax. Rest of the purpose and power is delegated 
to the programmer 
'''

# first_string = 'Does this string make '
# second_string = 'any sense to any of you sitting here now?'
# print(first_string+second_string)

'''
As you can see, the concatenation doesn't add any extra characters to the result. If you need 
punctuations, you need to add them wherever you need.

2. Formatting
==============
'''
# age = 23
# name = 'Sreendh TC'
# print('My name is %s and am %d years old!' % (name, age))

'''
This can also be done in a more pythonic way
'''
# bio = ('Sreenadh', 'TC', 23)
# bio_string = 'My name is %s %s and am %d years old!'
# print(bio_string % bio)

'''
3. Operations
==============
Length : the len() function
'''
# long_text = 'Duis velit eu nulla dolor non quis ad sunt do laboris occaecat sit velit.'
# print(len(long_text))

'''
Repeatition counting : the count() function
'''
# print(long_text.count('i'))
# print(long_text.count('lit'))

'''
Position of first occurence character in the whole string
'''
# print(long_text.index('i'))
# print(long_text.index('lit'))

'''
Replace character or word
'''
# print(long_text.replace('lit','out'))
# print(long_text)

'''
Now that is interesting, we told python to replace, it replaced, but we have an unchanged string? Why?

Well, python did replace those characters, but we didn't tell it where to save the changes to.
'''
# no_lit_long_text = long_text.replace('lit','out')
# print(no_lit_long_text)
