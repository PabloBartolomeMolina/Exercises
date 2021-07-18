# Functions to manipulate files

import matplotlib.pyplot as plt
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

    yes = 0
    no = 0
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        if line.__contains__('Yes'):
            print("Line{}: {}".format(count, line.strip()))
            yes += 1
        elif line.__contains__('No'):
            print("Line{}: {}".format(count, "No chance."))
            no += 1
    # Print results
    plot_search(yes, no)


def plot_search(p1, p2):
    t = [p1, p2]
    plt.plot(t, 'ro')
    names = ['yes', 'no']
    plt.scatter(names, t)
    plt.xlabel('Is people vaccinated ?')
    plt.ylabel('Number of persons.')
    plt.show()