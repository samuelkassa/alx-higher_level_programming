#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finding all multiples of 2 in the given list"""
    multiple_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiple_2.append(True)
        else:
            multiple_2.append(False)
    return (multiple_2)
