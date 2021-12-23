# Functions to treat files with information in hex format

import os.path


# Check format of file
def check_csv_format(path):
    # Check if it is possible to open the file.
    try:
        f = open(path, 'r')
        print("yay")
        flag_open = True
    except IOError:
        print("Oops, couldn't open the file")
        flag_open = False

    # Check if already in CSV format
    csv = False
    datafile = f.readlines()
    for line in datafile:
        if "," in line:
            csv = True
            break
    # Print result, mainly for debugging purposes.
    print ("CSV format ? ", csv)

    if flag_open:
        f.close()   # Close file if open
    else:
        pass        # File is not open

    return csv


# Convert file to CSV format
def set_csv_format(path):
    pass
