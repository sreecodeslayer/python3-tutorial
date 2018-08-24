'''
==============
Python File IO
==============
Files are one of the building blocks of persistend storage in Computers
We will see some of the basic files handling methods in Python
'''

'''
1. File name and Path
=====================
A typical file in any computing platform will have a name (w/ extension),
and a path to reach the file from root file system.
This is same for python as well. When we create a file,
the path and file name coexist.
'''
somefile = '/home/catman/Downloads/catman.txt'

'''
2. OS module
The OS module of python helps work with file paths and a lot of cool features
that OS already has to operate with on files.
Say like, rename, move, path, checking if a file exists and so on.
'''
import os

print('You application is currently running at path: %s' % os.getcwd())
print('Catman file exists? %s' % os.path.exists(somefile))
print('catman.txt is actually a file? %s' % os.path.isfile(somefile))

'''
1. Create, write and read
=========================
You can create a file just by using a random name.
Let's do it a bit professionally, so that no matter from where you run, the path is 
always relative to the working directory

File modes:
-----------
'r'     This is the default mode. It Opens file for reading.

'w'     This Mode Opens file for writing.
        If file does not exist, it creates a new file.
        If file exists it truncates the file.

'x'     Creates a new file. If file already exists, the operation fails.

'a'     Open file in append mode.
        If file does not exist, it creates a new file.

't'     This is the default mode. It opens in text mode.

'b'     This opens in binary mode.

'+'     This will open a file for reading and writing (updating)

eg.: 

ourfile = open(filename, mode)
'''
somefile_path = os.path.join(os.getcwd(), 'catman.txt')
'''
Create if not exist with any mode that involves a or w to 
'''
somefile = open(somefile_path, 'w+')

'''
Read when opened with mode r or + 
'''
print('Empty file ready: \n%s' % somefile.read())

'''
Write
'''
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
    " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."\
    " Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "\
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "\
    "reprehenderit in voluptate velit esse cillum dolore eu fugiat "\
    "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "\
    "sunt in culpa qui officia deserunt mollit anim id est laborum."

somefile.write(lorem_ipsum)
somefile.close()

'''
File context and 'with'

Context is like a closed scope area in python which closes itself outside
the indendation of the code snippet
'''
with open(somefile_path, 'w+') as somefile:
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"\
        " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."\
        " Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "\
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "\
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat "\
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, "\
        "sunt in culpa qui officia deserunt mollit anim id est laborum."

    somefile.write(lorem_ipsum)

'''
Note that we did not use a .close() as the with context will close the file as soon
as it gets out of context we are using 'somefile'
'''
