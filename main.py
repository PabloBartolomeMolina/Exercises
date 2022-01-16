# Main file of project with several exercises to improve skills on Python

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import files.
from files import *
from alarms import *
from psrGame import *
from cvManips import *
from myMath import *
import bytes_management as bm
import ListExercises as le

if __name__ == '__main__':
    path = "bytes_raw.txt"

    print("Test case 1:")
    le.shorted_list([1, 2, 3])
    print("\n"),
    print("Test case 2:")
    le.shorted_list([1, 2, 3, 4])
    print("\n")
    print("Test case 3:")
    le.shorted_list([1, 5, 2, 3])
    print("\n")
    print("Test case 4:")
    le.shorted_list([1, 3, 0, 5, 4])
    print("\n")
    print("Test case 5:")
    le.shorted_list([1, 2, 3, 3, 5])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
