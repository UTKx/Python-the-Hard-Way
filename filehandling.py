# Important file handling methods
# close: Closes the file. Like File->Save... in your editor.
# read: Reads the contents of the file. You can assign the result to a variable.
# readline: Reads just one line of a text file.
# truncate: Empties the file. Watch out if you care about the file.
# write('stuff'): Writes “stuff” to the file.
# seek(0): Moves the read/write location to the beginning of the file.

# from sys import argv

# script, filename = argv

# txt = open(filename)

# print(f"Here's your file {filename}:")
# print(txt.read())
# print("Type the filename again:")

# file_again = input("> ")
# txt_again = open(file_again)

# print(txt_again.read())
# print()

# Truncating a file
# from sys import argv

# script, filename = argv

# print(f"We're going to erase {filename}.")
# print("If you don't want that, hit CTRL-C (^C).")
# print("If you do want that, hit RETURN.")

# input("?")

# print("Opening the file...")

# target = open(filename, 'w')

# print("Truncating the file.Goodbye!")

# target.truncate()

# print("Now I'm going to ask you for three lines.")

# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")

# print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print("And finally, we close it.")
# target.close()

# Copying from one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}") # exists func checks whether the specified path exists or not
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


