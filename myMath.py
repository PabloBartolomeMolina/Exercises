from typing import List, Any, Union

import numpy as np
import math
from math import floor

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
    # print("Power is ", result)
    return result


def squared_root(base, margin):
    """
    Base : Number to calculate the squared root from.
    Margin : Precision for the result of the squared root calculation
    """
    # To calculate the SQRT, estimations are done. Starting with value 1.0.
    estimated = 1.0

    while abs(powered(estimated, 2) - base) >= margin:
        result = base / estimated
        med = (result + estimated) / 2.0;
        estimated = med

        '''
        #Debugging purposes
        print("Estimation :", estimated)
        print("SQRT :", result)'''

    # Adjust result to number of decimals coherent to input margin.
    decimals = estimated - floor(estimated)
    print("Result with all decimals :", estimated)
    marge = len(str(margin).split(".")[1])  # Limited to 4 decimals, to change if we want to have more precision.
    print("Decimals to take into account :", marge)
    estimated = round(float(estimated), marge) if len(str(estimated).split(".")[1]) > marge else estimated
    return estimated
