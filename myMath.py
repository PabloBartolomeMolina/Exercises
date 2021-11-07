from typing import List, Any, Union

import numpy as np
import math

def fibonacci(items):
    num_fibo: List[Union[int, Any]] = [0, 1]  # Basic Fibonacci sequence.

    if items <= 2:
        print(num_fibo)
    else:
        for x in range(2, items):
            # Index is not (items - 2) and (items - 1) to take into account the indexing system of Python
            num_fibo.append(num_fibo[x - 2] + num_fibo[x - 1])
        print(num_fibo)
        return num_fibo


def add_it_up(integer):
    if type(integer) == 'int':
        print("SUM is 0, no integer was given")
    else:
        sum = 0
        for x in range(0, integer + 1):
            sum = sum + x
        print("SUM is ", sum)
        return sum


def powered(base, index):
    if index == 0:
        result = 1
    else:
        result = base
        for x in range(1, index):
            result = result * base
    print("Power is ", result)
    return result


def squared_root(base):
    list_digits = list()
    result = 1
    rest = 0
    flag_continue = 0

    # Get number of digits of number to calculate squared root from.
    digits = int(math.log10(base)) + 1
    print("Number of digits", digits)
    # Separate digits into a list to properly calculate the squared root.
    if (digits % 2) == 0: # Par, even
        ''' Debugging purposes
        print("odd")
        print("", (digits % 2))
        print("", (digits / 2)+1)
        '''
        if digits == 2:
            list_digits.append(base)
        else:
            for i in range(0, digits, 2):
                list_digits.append(str(base)[i:i+2])

    else:               # Impar, odd
        print("even")
        list_digits.append(str(base)[0])  # First digit
        for i in range(1, digits, 2):
            list_digits.append(int(str(base)[i:i + 2]))
        pass

    print(list_digits)

    for i in range(len(list_digits)):
        for guess in range(1, base):
            computed = int(list_digits[i]) / powered(guess, 2)

            if computed > 1:
                # Squared root should be bigger
                pass
            elif computed == 1:
                # Exact result
                if i == 0:
                    result = guess
                else:
                    result = (result*10) + guess
                break
            else:
                if i == 0:
                    result = (guess - 1)
                else:
                    result = (result * 10) + (guess - 1)
                break

        print("Squared root is", result)
        print("Number to calculate squared root from is", base)
    return result
