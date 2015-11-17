# http://learnpythonthehardway.org/book/ex20.html


from sys import argv


script, input_file = argv

# define print

def print_all(f):
    # print the contents of f
    print(f.read())

# define the rewind function
def rewind(f):
    f.seek(0)

# define the print_a_line function, which takes 2 arguments (line_count, f)
def print_a_line(line_count, f):
    # print line_count
    print(line_count, f.readline())


current_file = open(input_file)

# print string
print("First let's print the whole file:\n")

# call function
print_all(current_file)

# print string
print("Now let's rewind, kind of like a tape.")


rewind(current_file)

# print string
print("Let's print three lines:")


current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)