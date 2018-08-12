'''
======================
Boolean in Python
======================

We will use this file to write a simple program that
explain the use and need of Boolean.
True or False
'''

print('1 EQUAL TO 1: ', 1 == 1)
print('1 NOT EQUAL TO 2: ', 1 != 2)
print('3 LESS THAN 4: ', 3 < 4)
print('4 GREATER THAN 5: ', 4 > 5)
print('5 LESS THAN or EQUAL TO 5: ', 5 <= 5)
print('6 GREATER THAN or EQUAL TO 5: ', 6 >= 5)

'''
AND, OR, and NOT operators in python
Just like the logic gates, we have the three logics in Python
'''
print('True OR False = ', (1 == 1) or (2 > 3))
print('True AND False = ', (1 == 1) and (2 > 3))
print('True OR (NOT False) = ', (1 == 1) or not (2 > 3))
print('True AND (NOT False) = ', (1 == 1) and not (2 > 3))

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

actual_user = 'sreenadh'


entered_name = input('Enter your username: ')
if actual_user == entered_name:
    print('Welcome, %s' % entered_name)


entered_name = input('Enter your username: ')
if actual_user == entered_name:
    print('Welcome, %s' % entered_name)
else:
    print("Sorry, I don't know you yet! Are you a new member?")
    new_user = input('Enter your username: ')
    new_password = input('Enter password: ')
    print('Welcome, %s' % new_user)


entered_name = input('Enter your username: ')
actual_password = 'givemeaccess'
if actual_user == entered_name:
    entered_passwd = input('Enter your password: ')
    if actual_password == entered_passwd:
        print('Welcome, %s' % entered_name)
    else:
        print('Wrong password, bye.')
else:
    print("Sorry, I don't know you yet! Are you a new member?")
    new_user = input('Enter your username: ')
    new_password = input('Enter password: ')
    print('Welcome, %s' % new_user)

first_user = 'sreenadh'
first_pass = 'access4sree'
second_user = 'mohandas'
second_pass = 'access4mohan'


entered_name = input('Enter your username: ')
if first_user == entered_name:
    entered_passwd = input('Enter your password: ')
    if first_pass == entered_passwd:
        print('Welcome, %s' % entered_name)
    else:
        print('Wrong password, bye.')
elif second_user == entered_name:
    entered_passwd = input('Enter your password: ')
    if second_pass == entered_passwd:
        print('Welcome, %s' % entered_name)
    else:
        print('Wrong password, bye.')
else:
    print("Sorry, I don't know you yet! Are you a new member?")
    new_user = input('Enter your username: ')
    new_password = input('Enter password: ')
    print('Welcome, %s' % new_user)
