# Functions to treat files with information in hex format

import os.path


# Check format of file
def check_csv_format(path):
    # Check if it is possible to open the file.
    try:
        f = open(path, 'r')
        print("yay")    # Debugging purposes
        flag_open = True
    except IOError:
        print("Oops, couldn't open the file")    # Debugging purposes
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
    # Check if it is possible to open the file.
    try:
        f = open(path, 'r')
        g = open("bytes_csv.txt", 'w')
        print("yay")        # Debugging purposes
        flag_open = True
    except IOError:
        print("Oops, couldn't open the file")       # Debugging purposes
        flag_open = False

    datafile = f.readlines()
    for line in datafile:
        g_line = line[0:4]  # Copy address
        i = 4   # Initial position for bytes after the 4 digits of address
        while i < 20:
            g_line = g_line + ','
            g_line = g_line + line[i:i+2]
            i += 2
        g_line = g_line + '\n'  # New line
        g.write(g_line)         # Copy into new file

    if flag_open:
        f.close()   # Close file if open
        g.close()   # Close file if open
    else:
        pass        # File is not open
