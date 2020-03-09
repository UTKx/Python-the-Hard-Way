# Functions and files

# from sys import argv

# script, input_file = argv

# def print_all(f):
#     print(f.read())

# def rewind(f):
#     f.seek(0)

# def print_a_line(line_count, f):
#     print(line_count, f.readline()) # > readline() reads one entire line from the fileA trailing newline character is kept in the string.
#                                     # > readline() function returns the \n
#                                     #   that’s in the file at the end of that line. 
#                                     #   Add a end = "" at the end of your print function calls
#                                     #   to avoid adding double \n to every line.

# current_file = open(input_file)

# print("First let's print the whole file:\n")

# print_all(current_file)

# print("Now let's rewind, kind of like a tape.")

# rewind(current_file)

# print("Let's print three lines:")

# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# Return
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
