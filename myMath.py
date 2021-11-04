from typing import List, Any, Union

import numpy as np


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
