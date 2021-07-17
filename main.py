# Main file of project with several exercises to improve skills on Python

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import files.
from files import *

if __name__ == '__main__':

    response = input("Persons vaccinated or not ? ")

    # Adapt input to standard word to be found in the csv file.
    if response == 'yes' or response == 'YES' or response == 'Yes' or response == 'YEs':
        response = 'Yes'
    elif response == 'no' or response == 'NO' or response == 'nO' or response == 'No':
        response = 'No'

    search_in_file('persons.csv', response)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
