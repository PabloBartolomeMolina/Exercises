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

    le.generate_3D_list(3, 6, 4)
    le.generate_3D_list(0, 6, 4)
    le.generate_3D_list(3, 0, 4)
    le.generate_3D_list(0, 0, 4)
    le.generate_3D_list(3, 6, 0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
