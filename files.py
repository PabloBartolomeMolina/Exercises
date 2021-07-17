# Functions to manipulate files

import os.path


def create_file(name):
    if not os.path.isfile(name):    # Create file only if not already existing.
        f = open(name, "x")     # Returns error if already existing.
    else:
        pass    # Nothing to be done if already existing.


def write_file(name, text):
    f = open(name, "w")
    f.write(text)
    f.close()


def read_file(name):
    f = open(name, "r")
    print(f.read())
    f.close()


def search_in_file(name, text):
    f = open(name, "r")
    lines = f.readlines()   # Get lines in the file.

    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        if line.__contains__(text):
            print("Line{}: {}".format(count, line.strip()))
        else:
            print("Line{}: {}".format(count, "No chance."))
