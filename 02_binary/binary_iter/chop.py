from math import floor
import ipdb

def chop(number, array):
    if not array or len(array)==0:
        return -1
    min_index = 0
    max_index = len(array)
    index = int(floor((min_index + max_index)/2))
    while array[index] != number and min_index < max_index:
        if number>array[index]:
            min_index = index + 1
        else:
            max_index = index - 1
        index = int(floor((min_index + max_index)/2))
    if array[index] == number:
        return index
    return -1
