from sys import argv

script, input_file = argv

def print_all(fl):
    print(fl.read())

def rewind(fl):
    print(">>> fl=", repr(fl))
    fl.seek(0)

def print_a_line(line_count, fl):
    print(line_count, fl.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
