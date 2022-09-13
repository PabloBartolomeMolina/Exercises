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
import myMath

if __name__ == '__main__':
    path = "bytes_raw.txt"

    print("Test case 1:")
    myMath.cartesian_distance([1, 1], [2, 2])
    print("Test case 2:")
    myMath.cartesian_distance([1, 1], [3, 3])
    print("Test case 3:")
    myMath.cartesian_distance([3, 3], [1, 1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
