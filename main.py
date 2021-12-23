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

if __name__ == '__main__':
    path = "bytes_raw.txt"

    format_csv = bm.check_csv_format(path)

    if not format_csv:
        bm.set_csv_format(path)
    else:
        pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
