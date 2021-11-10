# Main file of project with several exercises to improve skills on Python

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import files.
from files import *
from alarms import *
from psrGame import *
from cvManips import *
from myMath import *

if __name__ == '__main__':
    n = 1
    print("TEST NUMBER ", n)
    result = squared_root(6, 0.0001)
    print("Result ", result)
    n = n+1

    print("\n\nTEST NUMBER ", n)
    result = squared_root(10, 0.01)
    print("Result ", result)
    n = n + 1

    print("\n\nTEST NUMBER ", n)
    result = squared_root(1546, 0.0001)
    print("Result ", result)
    n = n + 1

    print("\n\nTEST NUMBER ", n)
    result = squared_root(154689, 0.000001)
    print("Result ", result)
    n = n + 1

    print("\n\nTEST NUMBER ", n)
    result = squared_root(121, 1)
    print("Result ", result)
    n = n + 1


    print("\n\nTEST NUMBER ", n)
    result = squared_root(12121, 0.0001)
    print("Result ", result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
