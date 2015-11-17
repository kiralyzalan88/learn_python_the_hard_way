


# http://learnpythonthehardway.org/book/ex16.html

__author__ = 'benedek balazs'

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # 'w' means that the pycharm will create or if you like write a file with the name that you have added earlier in Run > Edit Configurations > Script parameters

print("Truncating the file.  Goodbye!")
target.truncate() # ".trunctate()" means that all things will be deleted from the file.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n") # "\n" means new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
