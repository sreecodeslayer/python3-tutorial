'''
======================
Boolean in Python
======================

We will use this file to write a simple program that
explain the use and need of Boolean.
True or False
'''

# print('1 EQUAL TO 1: ', 1 == 1)
# print('1 NOT EQUAL TO 2: ', 1 != 2)
# print('3 LESS THAN 4: ', 3 < 4)
# print('4 GREATER THAN 5: ', 4 > 5)
# print('5 LESS THAN or EQUAL TO 5: ', 5 <= 5)
# print('6 GREATER THAN or EQUAL TO 5: ', 6 >= 5)

'''
AND, OR, and NOT operators in python
Just like the logic gates, we have the three logics in Python
'''
# print('True OR False = ', (1 == 1) or (2 > 3))
# print('True AND False = ', (1 == 1) and (2 > 3))
# print('True OR (NOT False) = ', (1 == 1) or not (2 > 3))
# print('True AND (NOT False) = ', (1 == 1) and not (2 > 3))

'''
Bool in python helps a programmer decide the flow of control.
The control of data, which set of code should execute,
and which should not.
That is what we are going to look into next.
Flow of control and Conditional Statements in Python
'''

'''
=========================
Flow of Control
=========================
Conditionals
1. if statement
2. if-else statement
3. if-elif statement
4. if-elif-else statement

Loops
1. while loop
2. for loop
3. break and continue
'''


'''
======================
Conditional statements
======================
'''

# actual_user = 'sreenadh'

# entered_name = input('Enter your username: ')
# if actual_user == entered_name:
#     print('Welcome, %s' % entered_name)


# entered_name = input('Enter your username: ')
# if actual_user == entered_name:
#     print('Welcome, %s' % entered_name)
# else:
#     print("Sorry, I don't know you yet! Are you a new member?")
#     new_user = input('Enter your username: ')
#     new_password = input('Enter password: ')
#     print('Welcome, %s' % new_user)


# entered_name = input('Enter your username: ')
# actual_password = 'givemeaccess'
# if actual_user == entered_name:
#     entered_passwd = input('Enter your password: ')
#     if actual_password == entered_passwd:
#         print('Welcome, %s' % entered_name)
#     else:
#         print('Wrong password, bye.')
# else:
#     print("Sorry, I don't know you yet! Are you a new member?")
#     new_user = input('Enter your username: ')
#     new_password = input('Enter password: ')
#     print('Welcome, %s' % new_user)

# first_user = 'sreenadh'
# first_pass = 'access4sree'
# second_user = 'mohandas'
# second_pass = 'access4mohan'


# entered_name = input('Enter your username: ')
# if first_user == entered_name:
#     entered_passwd = input('Enter your password: ')
#     if first_pass == entered_passwd:
#         print('Welcome, %s' % entered_name)
#     else:
#         print('Wrong password, bye.')
# elif second_user == entered_name:
#     entered_passwd = input('Enter your password: ')
#     if second_pass == entered_passwd:
#         print('Welcome, %s' % entered_name)
#     else:
#         print('Wrong password, bye.')
# else:
#     print("Sorry, I don't know you yet! Are you a new member?")
#     new_user = input('Enter your username: ')
#     new_password = input('Enter password: ')
#     print('Welcome, %s' % new_user)

'''
Note that Python does not offer 'switch' statement like in Java or C
Python believes that whatever switch does, you can easily do with a if-else 
combintations
'''
'''
======================
Loops in Python
======================

While loop
----------

While loop is the basic loop in python that lets the programmer
run a block of code untill a condition is met, ie. the condition 
that returns either a True or False.
'''

# spam = 0
# while spam < 10:
#     print('Spamming you %d times' % (spam+1))
#     spam += 1



'''
Let us write a small program that will continue adding your integer input
untill you tell it to stop
'''
# total = 0

# while True:
#     inp = input("Enter a number to add, N/n to stop: ")
#     try:
#         inp = int(inp)
#         total += inp
#     except ValueError:
#         if inp.lower() == 'n':
#             break
#         else:
#             continue
# print('Your total : ', total)

'''
For loop
----------

For loop is a limitting loop in python that lets the programmer
run a block of code within range condition, ie. the condition 
that returns an somekind iterable
'''
# for num in range(10):
#     print("Num : %s" % num)
