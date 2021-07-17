# Main file of project with several exercises to improve skills on Python

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import files.
from files import *

if __name__ == '__main__':
    create_file('testing.txt')
    write_file('testing.txt', 'Hello there!')
    read_file('testing.txt')

    search_in_file('testing.txt', 'Hello there!')
    search_in_file('testing.txt', 'Po-ta-toes!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
